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



# @frappe.whitelist(allow_guest=True)
# def submit_job_application(
#     first_name,
#     last_name,
#     email,
#     resume,
#     job_opening,
#     experience,
#     contact_number,
#     middle_name=None,
#     description=None
# ):
#     """
#     Submit a new Job Application.
#     Required:
#     - first_name, last_name, email, resume, job_opening, experience, contact_number
#     Optional:
#     - middle_name, description
#     """

#     try:
#         doc = frappe.get_doc({
#             "doctype": "Job Application",
#             "first_name": first_name,
#             "middle_name": middle_name or "",
#             "last_name": last_name,
#             "email": email,
#             "resume": resume,
#             "job_opening": job_opening,
#             "experience": experience,
#             "contact_number": contact_number,
#             "descriprion": description or ""
#         })

#         doc.insert(ignore_permissions=True)
#         frappe.db.commit()

#         return {
#             "status": "success",
#             "message": "Job application submitted successfully",
           
#         }

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "Submit Job Application API Error")
#         return {
#             "status": "error",
#             "message": str(e)
#         }

@frappe.whitelist(allow_guest=True)
def submit_job_application(
    first_name,
    last_name,
    email,
    experience,
    contact_number,
    job_opening,
    middle_name=None,
    description=None
):
    try:
        # Step 1: Get uploaded file
        resume_file = frappe.request.files.get("resume")
        file_doc_name = None

        if resume_file:
            file_doc = frappe.get_doc({
                "doctype": "File",
                "file_name": resume_file.filename,
                "attached_to_doctype": None,  # not attached yet
                "content": resume_file.read(),
                "is_private": 1
            })
            file_doc.insert(ignore_permissions=True)
            file_doc_name = file_doc.name

        # Step 2: Create Job Application with resume linked
        doc = frappe.get_doc({
            "doctype": "Job Application",
            "first_name": first_name,
            "middle_name": middle_name or "",
            "last_name": last_name,
            "email": email,
            "experience": experience,
            "contact_number": contact_number,
            "job_opening": job_opening,
            "descriprion": description or "",
            "resume": file_doc_name  # link file here
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()

        # Step 3: Attach file to this doc
        if file_doc_name:
            file_doc = frappe.get_doc("File", file_doc_name)
            file_doc.attached_to_doctype = "Job Application"
            file_doc.attached_to_name = doc.name
            file_doc.attached_to_field = "resume"
            file_doc.save(ignore_permissions=True)

        return {
            "status": "success",
            "message": "Job application submitted successfully"
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Submit Job Application API Error")
        return {
            "status": "error",
            "message": str(e)
        }
