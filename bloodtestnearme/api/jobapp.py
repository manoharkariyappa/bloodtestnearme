import frappe

@frappe.whitelist(allow_guest=True)
def get_job_openings(job_title=None):
    """
    Fetch Job Opening records.
    - No parameter → return ALL
    - With parameter → return ONLY matching record
    """

    filters = {"active": 1}

    # If parameter exists → filter by name (because name = job_title in your doctype)
    if job_title:
        filters["name"] = job_title

    try:
        data = frappe.get_all(
            "Job Opening",
            filters=filters,
            fields=["name", "job_title", "job_type", "description"],
            order_by="modified desc"
        )

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Job Opening API Error")
        return {
            "status": "error",
            "message": str(e)
        }



@frappe.whitelist(allow_guest=True)
def submit_job_application(
    first_name,
    last_name,
    email,
    resume,
    job_opening,
    experience,
    contact_number,
    middle_name=None,
    description=None
):
    """
    Submit a new Job Application.
    Required:
    - first_name, last_name, email, resume, job_opening, experience, contact_number
    Optional:
    - middle_name, description
    """

    try:
        doc = frappe.get_doc({
            "doctype": "Job Application",
            "first_name": first_name,
            "middle_name": middle_name or "",
            "last_name": last_name,
            "email": email,
            "resume": resume,
            "job_opening": job_opening,
            "experience": experience,
            "contact_number": contact_number,
            "descriprion": description or ""
        })

        doc.insert(ignore_permissions=True)
        frappe.db.commit()

        return {
            "status": "success",
            "message": "Job application submitted successfully",
           
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Submit Job Application API Error")
        return {
            "status": "error",
            "message": str(e)
        }
