# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in vanilla/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('vanilla/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='vanilla',
	version=version,
	description='Contains custom fields and custom scripts applicable to doctypes that come out of the box with ERPNext and Frappe',
	author='Xlevel Retail Systems Nig Ltd',
	author_email='tunde@francisakindele.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
