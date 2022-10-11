from __future__ import unicode_literals
import frappe
from datetime import datetime,date
from datetime import datetime

@frappe.whitelist()
def add_series_to_naming_series(pch_sc_item_series):
    print("....................",pch_sc_item_series)
    value = frappe.db.get_value("Naming Series","Naming Series","set_options")
    print("value",value)
    naming_seriesgs = frappe.get_doc('Naming Series')
    print("naming_seriesgs........",naming_seriesgs.set_options)
    frappe.client.set_value("Naming Series","Naming Series","select_doc_for_series","Item");
    series = naming_seriesgs.set_options+pch_sc_item_series
    print("series......",series)
    frappe.client.set_value("Naming Series","Naming Series","set_options",naming_seriesgs.set_options+pch_sc_item_series+"\n")    
    frappe.db.commit()