import json
import frappe
from frappe.utils import now_datetime

@frappe.whitelist(allow_guest=True)
def create_order():
    frappe.local.flags.ignore_csrf = True
    try:
        # Parse data from POST body (JSON)
        if frappe.request and frappe.request.data:
            data = json.loads(frappe.request.data)
        else:
            data = frappe.local.form_dict

        order = frappe.new_doc("Order")

        # Assign required fields
        order.customer_name = data.get("customer_name")
        order.age = data.get("age")
        order.email = data.get("email")
        order.mobile_number = data.get("mobile_number")
        order.address = data.get("address")
        order.gender = data.get("gender")
        order.pincode = data.get("pincode")
        order.doctor_name = data.get("doctor_name")
        order.technician_name = data.get("technician_name")
        order.comment = data.get("comment")
        order.appointment_date = data.get("appointment_date")
        order.appointment_time = data.get("appointment_time")
        order.number_of_persons = data.get("number_of_persons")
        order.total_item_price = data.get("total_item_price")
        order.total_price = data.get("total_price")
        order.affiliated_id = data.get("affiliated_id")
        order.hard_copy_required = data.get("hard_copy_required") or 0

        # Handle JSON field - Ordered Items
        ordered_items = data.get("ordered_items")
        if isinstance(ordered_items, (list, dict)):
            order.ordered_items = json.dumps(ordered_items)
        elif isinstance(ordered_items, str):
            order.ordered_items = ordered_items
        else:
            order.ordered_items = json.dumps([])

        # Handle LongText field - Customer Details
        customer_details = data.get("customer_details")
        if isinstance(customer_details, (list, dict)):
            order.customer_details = json.dumps(customer_details)
        else:
            order.customer_details = customer_details

        # Set default status as "Created"
        order.status = "Created"

        # Timestamps
        order.created_date = now_datetime()
        order.updated_date = now_datetime()

        # Insert into database
        order.insert(ignore_permissions=True)
        frappe.db.commit()

        # return {"status": "success", "Your order is Submitted Successfully": order.name1}
        return {"status": "success", "successmessage": "Your order is submitted successfully"}

    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(frappe.get_traceback(), "Create Order Error")
        return {"status": "error", "message": str(e)}
