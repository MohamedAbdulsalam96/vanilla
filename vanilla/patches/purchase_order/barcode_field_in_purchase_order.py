import frappe


def execute():
    frappe.reload_doc('buying', 'doctype', 'purchase_order')

    # Frappe names custom scripts as `[dt-Client]`. As long as this behavior
    # does not change, we are safe

    if not frappe.db.exists('Custom Script', 'Purchase Order-Client'):

        custom_script = frappe.new_doc('Custom Script')
        custom_script.dt = 'Purchase Order'
        custom_script.script = """
let go_ahead = 0;

frappe.ui.form.on('Purchase Order', {
    onload: function(frm) {
        frm.add_fetch("item_code", "item_name", "item_name");
        frm.events.listen_to(frm, 'quantity');
    },
    listen_to: function (frm, fieldname) {
        const fn = (e) => {
            if (frappe.ui.keys.key_map[e.which] === 'enter') {
                if (e.target.dataset.fieldname === fieldname) {
                    e.preventDefault();
                    frm.set_value(fieldname, '');	// otherwise we might not get change event to trigger
                    go_ahead = 1;
                    frm.set_value(fieldname, flt(e.target.value));
                }
            }
        }
        frappe.ui.keys.on('enter', fn);
    },
    barcode: function(frm) {
        if (frm.doc.barcode) {
            frappe.call({
                method: 'erpnext.stock.get_item_details.get_item_code',
                args: {'barcode': frm.doc.barcode},
                callback: function(r) {
                    if (!r.exe){
                        const item_code = r.message;
                        console.log(item_code);
                        const rows_with_item = frm.doc.items.filter(row => row.item_code === item_code);
                        console.log(rows_with_item);
                        const empty_rows = frm.doc.items.filter(row => !row.item_code);
                        console.log(empty_rows)
                        let chosen_row;

                        // empty table or filled up table without item
                        if ((!empty_rows.length && !rows_with_item.length) || !frm.doc.items.length) {
                            chosen_row = frm.add_child('items');
                        }
                        // if item is already in the table, use the first one, else use the first empty row we find
                        else {
                            chosen_row = rows_with_item.length ? rows_with_item[0] : empty_rows[0];
                        }
                        console.log(chosen_row);
                        go_ahead = 0;
                        frm.set_value('quantity', 1);
                        frappe.model.set_value(chosen_row.doctype, chosen_row.name, 'barcode', frm.doc.barcode);
                    }

                    frm.refresh_field('items');
                    $('input[data-fieldname="quantity"]').select();
                }
            });
        } else {
            frm.set_value('quantity', '');
        }
    },
    quantity: function(frm) {
        if (frm.doc.barcode && frm.doc.quantity && go_ahead) {
            const rows_with_item = frm.doc.items.filter(row => row.barcode === frm.doc.barcode);
            const empty_rows = frm.doc.items.filter(row => !row.item_code);
            let chosen_row;

            if ((!empty_rows.length && !rows_with_item.length) || !frm.doc.items.length) {
                chosen_row = frm.add_child('items');
            } else {
                chosen_row = rows_with_item ? rows_with_item[0] : empty_rows[0];
            }

            frappe.model.set_value(
                chosen_row.doctype,
                chosen_row.name,
                'qty',
                flt(chosen_row.qty) + flt(frm.doc.quantity)
            );

            go_ahead = 0;

            // let's clear the barcode for reuse
            frm.set_value('barcode', '');

            // reset the quantity field
            frm.set_value('quantity', '');

            // move focus back to the barcode field
            $('input[data-fieldname="barcode"]').select();
        }
    },
});
"""
    custom_script.insert(ignore_permissions=True)
