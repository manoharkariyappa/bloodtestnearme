import frappe

# @frappe.whitelist(allow_guest=True)
# def get_accepted_diagnostic_centers():
#     """
#     Returns all Diagnostic Centers with workflow_state = 'Accepted'
#     """
#     centers = frappe.get_all(
#         "Diagnostic Center",
#         filters={"workflow_state": "Accepted"},
#         fields=[
#             "name",
#             "diagnostic_center_name",
#             "workflow_state",
#             "address",
#             "city",
#             "state",
#             "pincode",
#             "phone_number",
#             "website",
#             "email_id",
#             "map_embed_link",
#             "blood_tests",
#             "health_checkups",
#             "ecg",
#             "scans",
#             "doctor_consultation",
#             "others",
#             "other_services_details",
#             "image"
#         ],
#         order_by="modified desc"
#     )
#     return centers

@frappe.whitelist(allow_guest=True)
def get_accepted_diagnostic_centers():
    """
    Public API to get Diagnostic Centers with workflow_state='Accepted'
    Optionally filters by pincode or city.
    Example:
      /api/method/bloodtestnearme.api.diagnostic_center.get_accepted_diagnostic_centers?pincode=560001
      /api/method/bloodtestnearme.api.diagnostic_center.get_accepted_diagnostic_centers?city=Bangalore
    """
    try:
        # Get query params (if provided)
        pincode = frappe.form_dict.get("pincode")
        city = frappe.form_dict.get("city")

        # Base filter
        filters = {"status": "Accepted"}

        # Add optional filters if present
        if pincode:
            filters["pincode"] = pincode
        if city:
            filters["city"] = city

        # Fetch matching records
        centers = frappe.get_all(
            "Diagnostic Center",
            filters=filters,
            fields=[
                "name",
                "diagnostic_center_name",
                "status",
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

        return {
            "status": "success",
            "total": len(centers),
            "filters_used": filters,
            "data": centers
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Accepted Diagnostic Centers Error")
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=True)
def create_diagnostic_center():
    """Public API to create Diagnostic Center without token"""
    try:
        data = frappe.request.get_json()
        if not data:
            frappe.throw(_("No JSON data provided."))

        required_fields = ["diagnostic_center_name", "address", "pincode", "city", "state", "phone_number"]

        for field in required_fields:
            if not data.get(field):
                frappe.throw(_(f"Missing required field: {field}"))

        doc = frappe.new_doc("Diagnostic Center")

        for field in required_fields:
            doc.set(field, data.get(field))

        optional_fields = [
            "website", "email_id", "image", "map_embed_link",
            "blood_tests", "health_checkups", "ecg",
            "scans", "doctor_consultation", "others", "other_services_details"
        ]

        for field in optional_fields:
            if field in data:
                doc.set(field, data.get(field))

        # ✅ Explicitly set workflow_state to "Created"
        doc.status = "Created"

        # Insert but don't submit
        doc.insert(ignore_permissions=True)

        return {
            "status": "success",
            "message": "Diagnostic Center created successfully",
            "name": doc.name,
            "status": doc.status
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Diagnostic Center Public API Error")
        return {"status": "error", "message": str(e)}
