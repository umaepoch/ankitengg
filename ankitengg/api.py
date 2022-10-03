from __future__ import unicode_literals
import frappe
from datetime import datetime,date
from datetime import datetime
#from __future__ import unicode_literals
#from frappe.model.naming import getseries
#import frappe, re
#from frappe.model.document import Document
#from frappe.model.naming import make_autoname

#@frappe.whitelist()
#def fetch_po_details(name):
#	print("name",name)
#	po_details=frappe.db.sql("""select supplier,address_display from `tabPurchase Order` where name ='"""+name+"""' """, as_dict=1)
#	print("po_details",po_details)
#	return po_details

#@frappe.whitelist()
#def set_supp_details_in_stock(name,purchase_order):
#    suplier =frappe.db.sql("""select supplier,supplier_address,address_display from `tabPurchase Order` where name ='"""+purchase_order+"""' """, as_dict=1)
#    stock = frappe.get_doc("Stock Entry",name)
#    stock.supplier_name = suplier[0].supplier
#    stock.supplier_address = suplier[0].supplier_address
#    stock.address_display = suplier[0].address_display
#    stock.save()
#    frappe.db.commit()
		
#bacancy 
@frappe.whitelist()
def fetch_item_group_parent(name):
	#print("name",name)
	details=frappe.db.sql("""select parent from `tabItem Group` where name IN (select parent from `tabItem Group` where name='"""+name+"""') """, as_dict=1)
	#print("details",details)
	return details

@frappe.whitelist()
def fetch_group_series_category(name):
	#print("name",name)
	series_category=frappe.db.sql("""select pch_sub_category,pch_sc_item_series from `tabItem Group` where name='"""+name+"""' """, as_dict=1)
	#print("series_category",series_category)
	return series_category

@frappe.whitelist()
def fetch_item_group_parent1(name):
	print("name of item group",name)
	details=frappe.db.sql("""select parent from `tabItem Group` where name IN (select parent from `tabItem Group` where name='"""+name+"""') """, as_dict=1)
	print("parent details",details)
	return details

@frappe.whitelist()
def fetch_parent(item_group):
    print("....................")
    print("name of first item ...........",item_group)
    details_First=frappe.db.sql("""select parent from `tabItem Group` where name ='"""+item_group+"""' """, as_dict=1)
    print("parent first details",details_First)
    return details_First

@frappe.whitelist()
def get_group_parent1(item_group):
    print("item_value",item_group)
    if item_group == "Resistors":
        print("RES")
        outerJson_b = {
        "doctype": "Document Naming Rule",
        "name":"",
        "document_type":"Item",
        "priority":0,
        "prefix":"RES-",
        "prefix_digits":4,
        "conditions": []
        }
        #print("outerJson",outerJson_b)
        for conditions in item_group:
            print("conditions",conditions)
            innerJson_b = {
            "field":"Item Group(item_group)",
            "condition":"=",
            "value":item_group,
            "doctype": "Document Naming Rule Condition"
            }
        outerJson_b['conditions'].append(innerJson_b)
        #print("inner",innerJson_b)
        #print("Outer Json",outerJson_b)
        doc = frappe.new_doc("Document Naming Rule")
        doc.update(outerJson_b)
        doc.save()
        print("doc",doc.name)
        print("doc............",doc.prefix)
        p_name = doc.prefix
        return p_name 
    elif item_group == "Capacitors":
        print("cap")
        outerJson_b = {
        "doctype": "Document Naming Rule",
        "name":"",
        "document_type":"Item",
        "priority":0,
        "prefix":"CAP-",
        "prefix_digits":4,
        "conditions": []
        }
        #print("outerJson",outerJson_b)
        for conditions in item_group:
            print("conditions",conditions)
            innerJson_b = {
            "field":"Item Group(item_group)",
            "condition":"=",
            "value":item_group,
            "doctype": "Document Naming Rule Condition"
            }
            outerJson_b['conditions'].append(innerJson_b)
            #print("inner",innerJson_b)
            #print("Outer Json",outerJson_b)
        doc = frappe.new_doc("Document Naming Rule")
        doc.update(outerJson_b)
        doc.save()
        print("doc",doc.name)
        print("doc............",doc.prefix)
        p_name = doc.prefix
        return p_name 