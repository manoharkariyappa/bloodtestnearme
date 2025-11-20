import frappe
import json
import smtplib
from email.mime.text import MIMEText


def send_direct_email(to_email, subject, html_message, sender):
    msg = MIMEText(html_message, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "wequantumberg@gmail.com"         
    SMTP_PASS = "kwoipnisqnwmmbyh"           
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.sendmail(sender, [to_email], msg.as_string())
    server.quit()


@frappe.whitelist(allow_guest=True)
def submit_contact():
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

  
    try:
        send_direct_email(
            to_email="wequantumberg@gmail.com",
            sender=email,
            subject=f"New Contact Form Submission from {name}",
            html_message=f"""
                <b>Name:</b> {name}<br>
                <b>Email:</b> {email}<br>
                <b>Phone:</b> {phone or '-'}<br>
                <b>How did you find us:</b> {source or '-'}
            """,
        )
    except Exception as e:
        return {"message": f"Email sending failed: {str(e)}"}

    return {"message": "success"}
