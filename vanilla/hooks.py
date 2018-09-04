# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "vanilla"
app_title = "Vanilla"
app_publisher = "Xlevel Retail Systems Nig Ltd"
app_description = "Contains custom fields and custom scripts applicable to doctypes that come out of the box with ERPNext and Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tunde@francisakindele.com"
app_license = "All rights reserved"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vanilla/css/vanilla.css"
# app_include_js = "/assets/vanilla/js/vanilla.js"

# include js, css files in header of web template
# web_include_css = "/assets/vanilla/css/vanilla.css"
# web_include_js = "/assets/vanilla/js/vanilla.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vanilla.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vanilla.install.before_install"
# after_install = "vanilla.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vanilla.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vanilla.tasks.all"
# 	],
# 	"daily": [
# 		"vanilla.tasks.daily"
# 	],
# 	"hourly": [
# 		"vanilla.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vanilla.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vanilla.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vanilla.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vanilla.event.get_events"
# }

