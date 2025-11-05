# Copyright (c) 2022, ALYF GmbH and contributors
# For license information, please see license.txt
from frappe.model.document import Document

from bloodtestnearme.qr_code import get_qr_code


class QRDemo(Document):
	def validate(self):
		self.qr_code = get_qr_code(self.title)
