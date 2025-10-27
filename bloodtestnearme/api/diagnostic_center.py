import frappe

@frappe.whitelist(allow_guest=True)
def get_accepted_diagnostic_centers():
    """
    Returns all Diagnostic Centers with workflow_state = 'Accepted'
    """
    centers = frappe.get_all(
        "Diagnostic Center",
        filters={"workflow_state": "Accepted"},
        fields=[
            "name",
            "diagnostic_center_name",
            "workflow_state",
            "address",
            "city",
            "state",
            "pincode",
            "phone_number",
            "website",
            "email_id",
            "map_embed_link",
            "blood_tests",
            "health_checkups",
            "ecg",
            "scans",
            "doctor_consultation",
            "others",
            "other_services_details",
            "image"
        ],
        order_by="modified desc"
    )
    return centers
