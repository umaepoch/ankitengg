from __future__ import unicode_literals
import frappe
from datetime import datetime,date
from datetime import datetime

@frappe.whitelist()
def add_series_to_naming_series(pch_sc_item_series):
    doc=frappe.get_doc("Naming Series")
    print("doc.set_options",doc.set_options)
    series = doc.set_options
    options = series.split("\n")
    print("options......1",options)
    print("pch_sc_item_series",pch_sc_item_series)
    options.append(pch_sc_item_series)
    print("options....2",options)
    doc.set_series_for("Item",options)
    doc.save()
    frappe.db.commit()
    print("options1",doc.get_options("Item"))   
    
