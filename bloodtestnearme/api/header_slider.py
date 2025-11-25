import frappe

@frappe.whitelist(allow_guest=True)
def get_header_sliders(slider_text=None):
    """
    Fetch all active Header Slider records
    Exact full match on slider_text if provided
    """
    try:
        if slider_text:
            sliders = frappe.get_list(
                "Header Slider",
                filters=[
                    ["active", "=", 1],
                    ["slider_text", "=", slider_text] 
                ],
                fields=["name", "slider_text", "link"],
                order_by="modified desc",
                ignore_permissions=True
            )
        else:
            sliders = frappe.get_list(
                "Header Slider",
                filters={"active": 1},
                fields=["name", "slider_text", "link"],
                order_by="modified desc",
                ignore_permissions=True
            )

        return {
            "status": "success",
            "count": len(sliders),
            "data": sliders
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Header Slider API Error")
        return {
            "status": "error",
            "message": str(e)
        }
