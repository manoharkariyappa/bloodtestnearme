import frappe
import json

@frappe.whitelist(allow_guest=True)
def submit_contact():
    # ✅ Optional: uncomment if you still get CSRFTokenError (for older Frappe builds)
    frappe.local.flags.ignore_csrf = True

    try:
        data = json.loads(frappe.request.data or '{}')
    except Exception:
        return {"message": "Invalid JSON data"}

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    source = data.get("source")

    if not (name and email):
        return {"message": "Name and Email are required"}

    frappe.sendmail(
        recipients=["wequantumberg@gmail.com"],
        sender=email,
        subject=f"New Contact Form Submission from {name}",
        message=f"""
            <b>Name:</b> {name}<br>
            <b>Email:</b> {email}<br>
            <b>Phone:</b> {phone or '-'}<br>
            <b>How did you find us:</b> {source or '-'}
        """,
    )

    return {"message": "✅ Message submitted successfully"}
