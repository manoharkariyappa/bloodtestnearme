app_name = "bloodtestnearme"
app_title = "Bloodtestnearme"
app_publisher = "Quantumberg Technologies Pvt Ltd"
app_description = "App to manage blood tests, labs, and patient bookings"
app_email = "admin@quantumberg.com"
app_license = "mit"

required_apps = ["frappe"]

modules = {
    "Bloodtestnearme": "bloodtestnearme.bloodtestnearme"
}



# app_requires = ["qrcode[pil]", "python-barcode~=0.15.1"]

# Apps
# ------------------
# 
# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "bloodtestnearme",
# 		"logo": "/assets/bloodtestnearme/logo.png",
# 		"title": "Bloodtestnearme",
# 		"route": "/bloodtestnearme",
# 		"has_permission": "bloodtestnearme.api.permission.has_app_permission"
# 	}
# ]
#from bloodtestnearme.api.swagger_ui import swaggerui_blueprint

#
override_whitelisted_methods = {
    "bloodtestnearme.api.pincodes_api.get_pincodes": "bloodtestnearme.api.pincodes_api.get_pincodes",
    "bloodtestnearme.api.search_api.global_quick_search": "bloodtestnearme.api.search_api.global_quick_search",
    "bloodtestnearme.api.testcenter_address.get_test_centers":"bloodtestnearme.api.testcenter_address.get_test_centers",
     "bloodtestnearme.api.testcenter_address.get_test_center":"bloodtestnearme.api.testcenter_address.get_test_center",
    "bloodtestnearme.api.packages.get_all_packages":"bloodtestnearme.api.packages.get_all_packages",
    "bloodtestnearme.api.packages.get_packages":"bloodtestnearme.api.packages.get_packages",
    "bloodtestnearme.api.packages.get_most_booking_packages": "bloodtestnearme.api.packages.get_most_booking_packages",
    "bloodtestnearme.api.packages.get_most_booking_tests": "bloodtestnearme.api.packages.get_most_booking_tests",
    "bloodtestnearme.api.packages.get_packages_by_category":"bloodtestnearme.api.packages.get_packages_by_category",
    "bloodtestnearme.api.packages.get_package_by_name":"bloodtestnearme.api.packages.get_package_by_name",
    "bloodtestnearme.api.diagnostic_center.get_accepted_diagnostic_centers": "bloodtestnearme.api.diagnostic_center.get_accepted_diagnostic_centers",
    "bloodtestnearme.api.diagnostic_center.create_diagnostic_center": "bloodtestnearme.api.diagnostic_center.create_diagnostic_center",

    "bloodtestnearme.api.order_api.create_order": "bloodtestnearme.api.order_api.create_order",
    "bloodtestnearme.api.certifications.get_certifications": "bloodtestnearme.api.certifications.get_certifications",
    "bloodtestnearme.api.packages.get_package_based_tests":"bloodtestnearme.api.packages.get_package_based_tests",    
    "bloodtestnearme.api.packages.get_individual_packages":"bloodtestnearme.api.packages.get_individual_packages",

}

# app_include_api = [
#     "bloodtestnearme.api.package"
# ]

# doc_events = {
#     "Affiliated Marketing": {
#         "before_save": "bloodtestnearme.bloodtestnearme.doctype.affiliated_marketing.affiliated_marketing.generate_qr"
#     }
# }


#app_include_blueprints = [swaggerui_blueprint]
#app_include_blueprints = ["bloodtestnearme.api.swagger_ui.get_blueprints"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bloodtestnearme/css/bloodtestnearme.css"
# app_include_js = "/assets/bloodtestnearme/js/bloodtestnearme.js"

# include js, css files in header of web template
# web_include_css = "/assets/bloodtestnearme/css/bloodtestnearme.css"
# web_include_js = "/assets/bloodtestnearme/js/bloodtestnearme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bloodtestnearme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "bloodtestnearme/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bloodtestnearme.utils.jinja_methods",
# 	"filters": "bloodtestnearme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bloodtestnearme.install.before_install"
# after_install = "bloodtestnearme.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bloodtestnearme.uninstall.before_uninstall"
# after_uninstall = "bloodtestnearme.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bloodtestnearme.utils.before_app_install"
# after_app_install = "bloodtestnearme.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bloodtestnearme.utils.before_app_uninstall"
# after_app_uninstall = "bloodtestnearme.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bloodtestnearme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bloodtestnearme.tasks.all"
# 	],
# 	"daily": [
# 		"bloodtestnearme.tasks.daily"
# 	],
# 	"hourly": [
# 		"bloodtestnearme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bloodtestnearme.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bloodtestnearme.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bloodtestnearme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bloodtestnearme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bloodtestnearme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bloodtestnearme.utils.before_request"]
# after_request = ["bloodtestnearme.utils.after_request"]

# Job Events
# ----------
# before_job = ["bloodtestnearme.utils.before_job"]
# after_job = ["bloodtestnearme.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bloodtestnearme.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

