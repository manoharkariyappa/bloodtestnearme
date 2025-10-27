import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def getby_pincodes(pincode=None):
    """
    Check if a specific pincode is active.
    If no pincode is provided, returns all active pincodes.
    """
    try:
        if pincode:
            exists = frappe.get_all(
                "Pincodes",
                filters={"pincode": pincode, "isactive": 1},
                fields=["name1", "state", "district"]
            )
            if exists:
                return {"status": "success", "message": "Service is available", "data": exists}
            else:
                return {"status": "error", "message": "Service not available for this pincode"}
        else:
            # Return all active pincodes
            pincodes = frappe.get_all(
                "Pincodes",
                filters={"isactive": 1},
                fields=["name1", "pincode", "state", "district"]
            )
            return {"status": "success", "data": pincodes}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Pincodes API Error")
        return {"status": "error", "message": str(e)}


@frappe.whitelist(allow_guest=True)
def get_pincodes():
    """
    Public API to fetch all active pincodes.
    Accessible by guest users (no login required).
    """
    try:
        # Fetch only active pincodes
        pincodes = frappe.get_all(
            "Pincodes",
            filters={"isactive": 1},
            fields=["name", "pincode", "state", "district"]
        )
        return {"status": "success", "data": pincodes}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Pincodes API Error")
        return {"status": "error", "message": str(e)}
