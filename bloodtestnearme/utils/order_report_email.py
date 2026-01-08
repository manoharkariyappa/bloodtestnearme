import frappe

def send_report_ready_email(doc, method=None):
    # 1️⃣ Get previous document state (VERY IMPORTANT)
    before = doc.get_doc_before_save()

    # If no previous version, this is a new document → skip
    if not before:
        return

    # If status did not change, skip
    if before.status == doc.status:
        return

    # Trigger ONLY when status changes TO Completed
    if doc.status != "Completed":
        return

    if not doc.email:
        return

    subject = f"Your Diagnostic Test Report - Order {doc.name}"

    message = frappe.render_template("""
<div style="max-width:650px;margin:0 auto;background:#ffffff;
border:1px solid #e5e7eb;border-radius:8px;
font-family:Arial,Helvetica,sans-serif;color:#111827;">

<!-- ================= HEADER ================= -->
<div style="padding:16px;border-bottom:1px solid #e5e7eb;">
  <h2 style="margin:0 0 6px 0;font-size:18px;">
    Your Diagnostic Test Report
  </h2>
  <p style="margin:0;font-size:13px;">
    Dear {{ doc.customer_name }},
  </p>
  <p style="margin:6px 0 0 0;font-size:13px;line-height:1.5;">
    Thank you for choosing our diagnostic services.
    Please find the diagnostic test reports for the beneficiaries listed below.
  </p>
</div>

<!-- ================= BENEFICIARY DETAILS ================= -->
<div style="padding:14px;">
  <div style="border:1px solid #d3d3d3;background:#f9fafb;border-radius:6px;padding:10px;">
    <h3 style="margin:0 0 8px 0;font-size:15px;">
      Beneficiary Details
    </h3>

    <ul style="margin:0;padding-left:16px;font-size:12px;line-height:1.5;">
    {% if doc.customer_details %}
      {% for row in doc.customer_details %}
        <li>
          {{ row.get("beneficiary_name") or row.get("name1") }}
          ({{ row.age }} Years, {{ row.gender }})
        </li>
      {% endfor %}
    {% else %}
      <li>{{ doc.customer_name }} ({{ doc.age }} Years, {{ doc.gender }})</li>
    {% endif %}
    </ul>
  </div>
</div>

<!-- ================= REPORT SUMMARY ================= -->
<div style="padding:14px;">
  <div style="border:1px solid #d3d3d3;background:#f9fafb;border-radius:6px;padding:10px;">
    <h3 style="margin:0 0 8px 0;font-size:15px;">
      Report Summary
    </h3>

    <ul style="margin:0;padding-left:14px;font-size:12px;line-height:1.5;">
      <li><b>Booking ID:</b> {{ doc.name }}</li>
      <li><b>Test / Package:</b>
        {% for item in doc.ordered_items %}
          {{ item.name1 }}{% if not loop.last %}, {% endif %}
        {% endfor %}
      </li>
      <li>
        <b>Total Beneficiaries:</b>
        {{ doc.customer_details|length if doc.customer_details else 1 }}
      </li>
    </ul>
  </div>
</div>

<!-- ================= IMPORTANT INFORMATION ================= -->
<div style="padding:14px;">
  <div style="border:1px solid #d3d3d3;background:#f9fafb;border-radius:6px;padding:10px;">
    <h3 style="margin:0 0 8px 0;font-size:15px;">
      Important Information
    </h3>

    <ul style="margin:0;padding-left:14px;font-size:12px;line-height:1.5;">
      <li>Diagnostic reports are attached with this email.</li>
      <li>Please consult your physician for medical interpretation.</li>
      <li>Reports are confidential and intended only for the recipients.</li>
    </ul>
  </div>
</div>

<!-- ================= FEEDBACK ================= -->
<div style="padding:14px;text-align:center;">
  <p style="margin:0 0 8px 0;font-size:13px;">
    Share Your Experience
  </p>
  <p style="margin:0 0 10px 0;font-size:12px;">
    Your feedback helps us improve our services.
  </p>

  <a href="https://www.trigunahealthcare.com/review"
     style="background:#2563eb;color:#ffffff;text-decoration:none;
     padding:8px 16px;border-radius:4px;font-size:12px;">
    Leave a Review
  </a>
</div>

<!-- ================= FOOTER TEXT ================= -->
<div style="padding:14px;font-size:12px;">
  <p style="margin:0;">
    If you have any questions regarding your reports,
    our support team will be happy to assist you.
  </p>
  <p style="margin:6px 0 0 0;">
    Best regards,<br>
    <b>Customer Support Team</b>
  </p>
</div>

<!-- ================= FOOTER ================= -->
<div style="background:#1e3a8a;padding:18px 12px;text-align:center;
border-radius:0 0 8px 8px;">

  <div style="margin-bottom:12px;">
    <a href="tel:+919999999999"
       style="background:#2563eb;color:#ffffff;text-decoration:none;
       padding:8px 16px;border-radius:4px;font-size:12px;margin-right:6px;">
      Call Now
    </a>
    <a href="https://wa.me/919999999999"
       style="background:#22c55e;color:#ffffff;text-decoration:none;
       padding:8px 16px;border-radius:4px;font-size:12px;">
      WhatsApp
    </a>
  </div>

  <div style="margin-bottom:8px;">
    <img src="{{ frappe.utils.get_url() }}/files/trigunalogo.png"
         style="max-width:160px;background:#ffffff;
         padding:6px;border-radius:6px;">
  </div>

  <p style="margin:4px 0;font-size:11px;color:#dbeafe;">
    © {{ frappe.utils.nowdate()[:4] }} Triguna Healthcare. All rights reserved.
  </p>

  <p style="margin:0;font-size:10px;color:#9ca3af;">
    This communication is confidential and intended solely for the recipients.
  </p>
</div>

</div>
""", {"doc": doc})

    frappe.sendmail(
        recipients=[doc.email],
        subject=subject,
        message=message,
        now=True
    )
