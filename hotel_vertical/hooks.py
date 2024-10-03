app_name = "hotel_vertical"
app_title = "Hotel Vertical"
app_publisher = "Ketan Patel"
app_description = "Hotel Management to Manage Folio and Hotel Configuration"
app_email = "contact@solufy.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hotel_vertical/css/hotel_vertical.css"
# app_include_js = "/assets/hotel_vertical/js/hotel_vertical.js"

# include js, css files in header of web template
# web_include_css = "/assets/hotel_vertical/css/hotel_vertical.css"
# web_include_js = "/assets/hotel_vertical/js/hotel_vertical.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hotel_vertical/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/custom_sales_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hotel_vertical/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hotel_vertical.utils.jinja_methods",
#	"filters": "hotel_vertical.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hotel_vertical.install.before_install"
# after_install = "hotel_vertical.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hotel_vertical.uninstall.before_uninstall"
# after_uninstall = "hotel_vertical.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hotel_vertical.utils.before_app_install"
# after_app_install = "hotel_vertical.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hotel_vertical.utils.before_app_uninstall"
# after_app_uninstall = "hotel_vertical.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hotel_vertical.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# doc_events = {
#     "Sales Order": {
#         "on_update": "hotel_vertical.public.py.custom_sales_order.create_kot_history"
#     }
# }



# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"hotel_vertical.tasks.all"
#	],
#	"daily": [
#		"hotel_vertical.tasks.daily"
#	],
#	"hourly": [
#		"hotel_vertical.tasks.hourly"
#	],
#	"weekly": [
#		"hotel_vertical.tasks.weekly"
#	],
#	"monthly": [
#		"hotel_vertical.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "hotel_vertical.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "hotel_vertical.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hotel_vertical.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hotel_vertical.utils.before_request"]
# after_request = ["hotel_vertical.utils.after_request"]

# Job Events
# ----------
# before_job = ["hotel_vertical.utils.before_job"]
# after_job = ["hotel_vertical.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hotel_vertical.auth.validate"
# ]

fixtures = [
    {
        "doctype": "Website Settings",
        "filters": {}
    },
    {
    "doctype": "Workspace",
        "filters": [
            [
                "name", "in", [
                    "Hotel Vertical"
                ]
            ]
        ]
    },
    {
    "doctype": "Workflow",
        "filters": [
            [
                "name", "in", [
                    "Table Booking Workflow", "KOT Workflow", "Banquet Booking Workflow"
                ]
            ]
        ]
    },
    {
    "doctype": "Workflow State",
    }

]
