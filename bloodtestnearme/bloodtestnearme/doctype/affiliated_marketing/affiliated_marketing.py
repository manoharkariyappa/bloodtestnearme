import frappe
import qrcode
import io
import base64
from frappe.model.document import Document

class AffiliatedMarketing(Document):
    def before_save(self):
        # Text to encode in the QR
        qr_text = f"Affiliate: {self.affiliate_name}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR image to memory
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        # Save file to Frappe File system
        file_doc = frappe.get_doc({
            "doctype": "File",
            "file_name": f"{self.affiliate_name}_qr.png",
            "attached_to_doctype": self.doctype,
            "attached_to_name": self.name,
            "content": base64.b64encode(buf.getvalue()).decode("utf-8"),
            "decode": True
        })
        file_doc.save(ignore_permissions=True)

        # Save the URL directly to the Attach Image field
        self.qr_code = file_doc.file_url
        self.qr_code_url = qr_text
