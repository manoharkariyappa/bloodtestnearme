# File: bloodtestnearme/api.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_certifications():

    try:
        certifications = frappe.get_all(
            "Certifications",
            filters={"is_active": 1},
            fields=["name", "title", "image", "is_active"],
            order_by="creation desc"
        )
        return {
            "status": "success",
            "count": len(certifications),
            "data": certifications
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_certifications API Error")
        return {
            "status": "error",
            "message": str(e)
        }
