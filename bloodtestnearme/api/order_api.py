# import json
# import frappe
# from frappe.utils import now_datetime

# @frappe.whitelist(allow_guest=True)
# def create_order():
#     frappe.local.flags.ignore_csrf = True
#     try:
#         # Parse data from POST body (JSON)
#         if frappe.request and frappe.request.data:
#             data = json.loads(frappe.request.data)
#         else:
#             data = frappe.local.form_dict

#         order = frappe.new_doc("Order")

#         # Assign required fields
#         order.customer_name = data.get("customer_name")
#         order.age = data.get("age")
#         order.email = data.get("email")
#         order.mobile_number = data.get("mobile_number")
#         order.address = data.get("address")
#         order.gender = data.get("gender")
#         order.pincode = data.get("pincode")
#         order.doctor_name = data.get("doctor_name")
#         order.technician_name = data.get("technician_name")
#         order.comment = data.get("comment")
#         order.appointment_date = data.get("appointment_date")
#         order.appointment_time = data.get("appointment_time")
#         order.number_of_persons = data.get("number_of_persons")
#         order.total_item_price = data.get("total_item_price")
#         order.total_price = data.get("total_price")
#         order.affiliated_id = data.get("affiliated_id")
#         order.hard_copy_required = data.get("hard_copy_required") or 0

#         # Handle JSON field - Ordered Items
#         ordered_items = data.get("ordered_items")
#         if isinstance(ordered_items, (list, dict)):
#             order.ordered_items = json.dumps(ordered_items)
#         elif isinstance(ordered_items, str):
#             order.ordered_items = ordered_items
#         else:
#             order.ordered_items = json.dumps([])

#         # Handle LongText field - Customer Details
#         customer_details = data.get("customer_details")
#         if isinstance(customer_details, (list, dict)):
#             order.customer_details = json.dumps(customer_details)
#         else:
#             order.customer_details = customer_details

#         # Set default status as "Created"
#         order.status = "Ordered"
#         order.order_type = "Online"
#         # Timestamps
#         order.created_date = now_datetime()
#         order.updated_date = now_datetime()

#         # Insert into database
#         order.insert(ignore_permissions=True)
#         frappe.db.commit()

#         # return {"status": "success", "Your order is Submitted Successfully": order.name1}
#         return {"status": "success", "successmessage": "Your order is submitted successfully"}

#     except Exception as e:
#         frappe.db.rollback()
#         frappe.log_error(frappe.get_traceback(), "Create Order Error")
#         return {"status": "error", "message": str(e)}



# import json
# import frappe
# from frappe.utils import now_datetime

# @frappe.whitelist(allow_guest=True)
# def create_order():
#     frappe.local.flags.ignore_csrf = True
#     try:
#         # Parse POST JSON
#         if frappe.request and frappe.request.data:
#             data = json.loads(frappe.request.data)
#         else:
#             data = frappe.local.form_dict

#         order = frappe.new_doc("Order")

#         # Assign simple fields
#         order.customer_name = data.get("customer_name")
#         order.age = data.get("age")
#         order.email = data.get("email")
#         order.mobile_number = data.get("mobile_number")
#         order.address = data.get("address")
#         order.gender = data.get("gender")
#         order.pincode = data.get("pincode")
#         order.doctor_name = data.get("doctor_name")
#         # order.technician_name = data.get("technician_name")
#         order.comment = data.get("comment")
#         order.appointment_date = data.get("appointment_date")
#         order.appointment_time = data.get("appointment_time")
#         order.number_of_persons = data.get("number_of_persons")
#         order.total_item_price = data.get("total_item_price")
#         order.total_price = data.get("total_price")
#         order.affiliated_id = data.get("affiliated_id")
#         order.hard_copy_required = data.get("hard_copy_required") or 0

#         # -----------------------------
#         # ✅ Insert CHILD TABLE rows
#         # -----------------------------
#         # ordered_items = data.get("ordered_items", [])
#         # if isinstance(ordered_items, list):
#         #     for item in ordered_items:
#         #         order.append("ordered_items", {
#         #             "test_name": item.get("name1"),
#         #             "price": item.get("price")
#         #         })
#         # ----- CHILD TABLE -----
#         ordered_items = data.get("ordered_items", [])

#         if isinstance(ordered_items, list):
#          for item in ordered_items:
#              order.append("ordered_items", {
#             "name1": item.get("name1"),
#             "price": item.get("price")
#             })


#         # -----------------------------
#         # Handle customer details
#         # -----------------------------
#         customer_details = data.get("customer_details")
#         if isinstance(customer_details, (list, dict)):
#             order.customer_details = json.dumps(customer_details)
#         else:
#             order.customer_details = customer_details

#         # Defaults
#         order.status = "Ordered"
#         order.order_type = "Online"
#         order.created_date = now_datetime()
#         order.updated_date = now_datetime()

#         # Save document
#         order.insert(ignore_permissions=True)
#         frappe.db.commit()

#         return {
#             "status": "success",
#             "successmessage": "Your order is submitted successfully",
#             "order_id": order.name
#         }

#     except Exception as e:
#         frappe.db.rollback()
#         frappe.log_error(frappe.get_traceback(), "Create Order Error")
#         return {"status": "error", "message": str(e)}

import frappe

@frappe.whitelist(allow_guest=True)
def get_orders(status=None, order_type=None):

    try:
        filters = {}

        if status:
            filters["status"] = status

        orders = frappe.get_all(
            "Order",
            filters=filters,
            fields=[
                "name",
                "appointment_date",
                "appointment_time",
                "customer_name",
                "pincode",
                "total_price",
                "mobile_number",
                "status"
            ],
            order_by="creation desc"
        )

        return {
            "status": "success",
            "data": orders
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Orders Error")
        return {
            "status": "error",
            "message": str(e)
        }

import frappe
@frappe.whitelist(allow_guest=True)
def get_offline_orders(status=None):

    try:
        filters = {}

        if status:
            filters["status"] = status

        orders = frappe.get_all(
            "Offline Order",
            filters=filters,
            fields=[
                "name",
                "appointment_date",
                "appointment_time",
                "customer_name",
                "total_price",
                "mobile_number",
                "status"
            ],
            order_by="creation desc"
        )

        return {
            "status": "success",
            "data": orders
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Orders Error")
        return {
            "status": "error",
            "message": str(e)
        }

import json
import frappe
from frappe.utils import now_datetime

@frappe.whitelist(allow_guest=True)
def create_order():
    frappe.local.flags.ignore_csrf = True
    
    try:
        # Parse POST JSON
        if frappe.request and frappe.request.data:
            data = json.loads(frappe.request.data)
        else:
            data = frappe.local.form_dict

        order = frappe.new_doc("Order")

        # Assign simple fields
        order.customer_name = data.get("customer_name")
        order.age = data.get("age")
        order.email = data.get("email")
        order.mobile_number = data.get("mobile_number")
        order.address = data.get("address")
        order.gender = data.get("gender")
        order.pincode = data.get("pincode")
        order.doctor_name = data.get("doctor_name")
        order.comment = data.get("comment")
        order.appointment_date = data.get("appointment_date")
        order.appointment_time = data.get("appointment_time")
        order.number_of_persons = data.get("number_of_persons")
        order.total_item_price = data.get("total_item_price")
        order.total_price = data.get("total_price")
        order.affiliated_id = data.get("affiliated_id")
        order.hard_copy_required = data.get("hard_copy_required") or 0

        # -------------------------------------------------------------------
        # ✅ INSERT ORDERED ITEMS CHILD TABLE
        # -------------------------------------------------------------------
        ordered_items = data.get("ordered_items", [])
        if isinstance(ordered_items, list):
            for item in ordered_items:
                order.append("ordered_items", {
                    "name1": item.get("name1"),
                    "price": item.get("price"),
                })

        # -------------------------------------------------------------------
        # ✅ INSERT CUSTOMER DETAILS CHILD TABLE
        # -------------------------------------------------------------------
        customer_details = data.get("customer_details", [])
        if isinstance(customer_details, list):
            for cust in customer_details:
                order.append("customer_details", {
                    "name1": cust.get("name"),
                    "age": cust.get("age"),
                    "gender": cust.get("gender"),
                })

        # -------------------------------------------------------------------
        # ✅ INSERT TECHNICIAN NAME (TABLE MULTISELECT)
        # -------------------------------------------------------------------
        technician_list = data.get("technician_name", [])
        if isinstance(technician_list, list):
            for tech in technician_list:
                order.append("technician_name", {
                    "user": tech.get("user")  # field inside User Group Member
                })

        # Defaults
        order.status = "Ordered"
        order.order_type = data.get("order_type") or "Online"
        order.created_date = now_datetime()
        order.updated_date = now_datetime()

        # Save
        order.insert(ignore_permissions=True)
        frappe.db.commit()

        return {
            "status": "success",
            "successmessage": "Order created successfully",
            # "order_id": order.name
        }

    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(frappe.get_traceback(), "Create Order Error")
        return {"status": "error", "message": str(e)}
