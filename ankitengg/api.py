from __future__ import unicode_literals
import frappe
from datetime import datetime,date
from datetime import datetime
#from __future__ import unicode_literals
#from frappe.model.naming import getseries
#import frappe, re
#from frappe.model.document import Document
#from frappe.model.naming import make_autoname

@frappe.whitelist()
def get_stock_qty(item_code,warehouse):
    print("entered in get_stock_qty function")
    qty = frappe.db.sql("""select concat_ws(" ", posting_date, posting_time) as date,qty_after_transaction from `tabStock Ledger Entry` where item_code='"""+item_code+"""' and warehouse='"""+warehouse+"""' order by posting_date,posting_time """, as_dict=1)
    print("quantity",qty)
    return qty

@frappe.whitelist()
def fetch_acc_dimension_company():
    company=frappe.db.sql("""select company from `tabAccounting Dimension Detail` as adetail join `tabAccounting Dimension` as ad on ad.name = adetail.parent""", as_dict=1)
    print("company_details",company)
    return company 

#@frappe.whitelist()
#def send_email(email_address):
#    print("0000000000000000name",email_address)
#    frappe.sendmail(recipients=email_address,
#    sender="pavithra@meritsystems.com",
#	subject="Subject of the email",
#	message= "Content of the email")
    
#def sendmail():
#    user_list = frappe.db.sql("""select name, employee_name from `tabEmployee` where designation = "Batch Supervisor";""")
#    for user_obj in user_list:
#        user = user_obj[0];
#        employee = user_obj[1];
#        content = "<h4>Hello, "+ employee +"</h4><p>Following Batch will be expiry soon. Please make a note for that.</p><table class='table table-bordered'><tr><th>Batch Number</th><th>Expiry Date</th></tr>"
#        batch_list = frappe.db.sql("""select batch_id, expiry_date  from `tabBatch` where DATEDIFF(expiry_date, CURRENT_DATE()) < 30;""")
#        for batch_obj in batch_list:
#            batch = batch_obj[0]
#            expiry_date = str(batch_obj[1].strftime('%d/%m/%Y'))
#            content = content + "<tr><td>"+batch+"</td><td>"+expiry_date+"</td></tr>"         
#            content = content + "</table>"
#            recipient = frappe.get_value("Employee", user, "prefered_email")
#            frappe.sendmail(recipients=[recipient],
#            sender="pavithra@meritsystems.com",
#            subject="Item Batch To Be Expire", content=content)

@frappe.whitelist()
def send_email_for_due_date():
    message = " "
    next_actions_list = frappe.db.get_list('ToDo',fields=['*'],filters={})
    for action in next_actions_list :    
        posting_date= action.date
        p_date = str(posting_date)
        now = datetime.now()
        current_dte = now.strftime("%Y-%m-%d")
        time_format = '%Y-%m-%d'
        no_of_days = datetime.strptime(p_date, time_format) - datetime.strptime(current_dte, time_format)
        owner = action.owner
        owner = owner.split()
        for own in owner :
            full_name = frappe.db.get_list("User",filters={"name":own},fields=["full_name"]) 
        if no_of_days.days == 0:
            subject = """ ALERT, Task """+action.pch_subject+""" is due today """+p_date+""" """
            message = """ Hai """+full_name[0].full_name+""" , <br><br> Task No """+action.name+""" , """+action.pch_subject+""" has been assigned to you and is: 
            due today """+p_date+""" <br><br> Please ensure that you complete this task and update on ERPNext that you have completed the task. <br><br>
            Since this task is: due today , please meet Kapil Gupta and/or Ajay Tickoo and discuss what support you need to complete the task today.<br>
            """                    
            print("message",message)
            recipients= action.pch_recipient_list
            print("recipients",recipients)
            print("subject",subject)
            frappe.sendmail(
            recipients= recipients,
            subject=subject,
            message=message
            )
        if no_of_days.days < 0:
            subject = """ ALERT, Task """+action.pch_subject+""" is due on """+p_date+""" """
            message = """ Hai """+full_name[0].full_name+""" ,<br><br> Task No """+action.name+""" , """+action.pch_subject+""" has been assigned to you and is: 
            Overdue("""+p_date+""") <br><br>
            Since this task is: Overdue , please meet Kapil Gupta and/or Ajay Tickoo and discuss what support you need to complete the task today.<br><br>
            please meet Kapil Gupta and/or Ajay Tickoo today without fail and discuss how you are going to complete the task today. Not completing the task today may invite disciplinary action."""                    
            print("message",message)
            recipients= action.pch_recipient_list
            print("recipients",recipients)
            print("subject",subject)
            frappe.sendmail(
            recipients= recipients,
            subject=subject,
            message=message
            )
        if no_of_days.days == 1:
            subject = """ ALERT, Task """+action.pch_subject+""" is due on """+p_date+""" """
            message = """ Hai """+full_name[0].full_name+""" ,<br><br> 
            Task No """+action.name+""" , """+action.pch_subject+""" has been assigned to you and is: 
            due tomorrow ("""+p_date+""") <br><br> 
            Please ensure that you complete this task and update on ERPNext that you have completed the task.
            """                    
            print("message",message)
            recipients= action.pch_recipient_list
            print("recipients",recipients)
            print("subject",subject)
            frappe.sendmail(
            recipients= recipients,
            subject=subject,
            message=message
            )
        if no_of_days.days > 1:
            subject = """ ALERT, Task """+action.pch_subject+""" is s due on """+p_date+"""  <br><br> """
            message = """ Hai """+full_name[0].full_name+""" ,<br><br> 
            Task No """+action.name+""" , """+action.pch_subject+""" has been assigned to you and is: 
            due on ("""+p_date+""") <br><br> 
            Please ensure that you complete this task and update on ERPNext that you have completed the task.<br><br> 
            """                    
            print("message",message)
            recipients= action.pch_recipient_list
            print("recipients",recipients)
            print("subject",subject)
            frappe.sendmail(
            recipients= recipients,
            subject=subject,
            message=message
            )

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