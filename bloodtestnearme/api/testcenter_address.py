import frappe

@frappe.whitelist(allow_guest=True)
def get_test_centers():
    """Return all active Test Center Addresses."""
    centers = frappe.get_all(
        "Test Center Address",
        fields=[
            "name",
            "test_center_name",
            "branch_name",
            "address_line",
            "pincode",
            "city",
            "state",
            "contact_number",
            "alternate_contact_number",
            "email_id",
            "map_embed_link",
            "timings",
            "image"
        ],
    )
    return centers


@frappe.whitelist(allow_guest=True)
def get_test_center(pincode=None, branch_name=None):
    """
    Fetch Test Center Address records.
    - If pincode is provided → filter by pincode
    - If branch_name is provided → filter by branch name
    - If neither provided → return all
    """

    filters = {}

    if pincode:
        filters["pincode"] = pincode
    elif branch_name:
        filters["branch_name"] = branch_name

    try:
        data = frappe.get_all(
            "Test Center Address",
            filters=filters,
            fields=[
                "name",
                "test_center_name",
                "branch_name",
                "address_line",
                "pincode",
                "city",
                "state",
                "contact_number",
                "alternate_contact_number",
                "email_id",
                "map_embed_link",
                "timings",
                "image"
            ]
        )

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Test Center API Error")
        return {
            "status": "error",
            "message": str(e)
        }

