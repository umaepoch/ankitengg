import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def create_fixtures():
    create_fields()


def create_fields():
    custom_fields = {
        "Account": [
            {
                "fieldname": "pch_opening_month_only",
                "label": "Report Opening Month of Period Only",
                "fieldtype": "Check",
                "depends_on": "eval: !doc.is_group",
                "insert_after": "inter_company_account",
            },
            {
                "fieldname": "pch_closing_month_only",
                "label": "Report Closing Month of Period Only",
                "fieldtype": "Check",
                "depends_on": "eval: !doc.is_group",
                "insert_after": "pch_opening_month_only",
            },
        ]
    }

    create_custom_fields(custom_fields)
