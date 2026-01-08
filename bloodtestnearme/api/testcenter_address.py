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
            "image",
            "description",
            "url",
            "meta_title",
            "meta_description"
        ],
        order_by="order_sequence asc"
    )
    return centers


@frappe.whitelist(allow_guest=True)
def get_test_center(pincode=None, branch_name=None, test_center_name=None, url=None):
    """
    Fetch Test Center Address records with optional filters:
    - pincode
    - branch_name
    - test_center_name
    """

    filters = {}

    if pincode:
        filters["pincode"] = pincode
    if branch_name:
        filters["branch_name"] = branch_name
    if test_center_name:
        filters["test_center_name"] = test_center_name
    if url:
        filters["url"] = url

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
                "image",
                "description",
                "url",
                "meta_title",
                "meta_description"
            ],
            order_by="order_sequence asc"
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
