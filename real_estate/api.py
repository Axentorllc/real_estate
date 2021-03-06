from __future__ import unicode_literals

import frappe
import frappe.defaults
from frappe.utils import cstr, flt, fmt_money, formatdate, getdate
from frappe.utils import (cint, split_emails, get_request_site_address, cstr,get_files_path, get_backups_path, get_url, encode)
from frappe import _


@frappe.whitelist(allow_guest=True)
def generate_lead(name,email,phone,for_property,note=None):
	d = frappe.new_doc('Lead')
	d.lead_name = name
	d.email_id = email
	d.phone = phone
	d.remark = note
	d.for_property = for_property
	d.insert(ignore_permissions=True)
	return d.name


@frappe.whitelist()
def import_french_translation():
	frappe.db.sql('delete from `tabTranslation`')
	from frappe.core.doctype.data_import.data_import import import_file_by_path
	import_file_by_path(path=frappe.utils.get_bench_path()+'/apps/real_estate/real_estate/public/translation/Translation.csv',ignore_links=False, overwrite=True,submit=False, pre_process=None, no_email=True)
