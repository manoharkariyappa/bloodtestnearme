import frappe
from flask_swagger_ui import get_swaggerui_blueprint

# Custom URL for Swagger
SWAGGER_URL = '/bloodtestnearme-swagger'  # 👈 custom route name
API_URL = '/api/method/bloodtestnearme.api.swagger_ui.get_openapi_spec'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Blood Test Near Me API Docs"}
)

def get_blueprints():
    """Expose Swagger UI blueprint"""
    return [swaggerui_blueprint]


@frappe.whitelist(allow_guest=True)
def get_openapi_spec():
    """Generate OpenAPI spec dynamically from hooks.override_whitelisted_methods"""
    from importlib import import_module

    app_name = "bloodtestnearme"
    app_hooks = import_module(f"{app_name}.hooks")
    methods = getattr(app_hooks, "override_whitelisted_methods", {})

    paths = {}

    for full_path, method_path in methods.items():
        parts = method_path.split(".")
        func_name = parts[-1]
        endpoint = f"/api/method/{method_path}"

        paths[endpoint] = {
            "get": {
                "summary": f"{func_name.replace('_', ' ').title()}",
                "operationId": func_name,
                "responses": {
                    "200": {"description": "Successful response"}
                },
                "parameters": [
                    {
                        "name": "params",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "string"},
                        "description": "Optional parameters (depends on API)"
                    }
                ]
            }
        }

    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Blood Test Near Me API",
            "version": "1.0.0",
            "description": "Auto-generated Swagger docs for all Frappe APIs in this app."
        },
        "paths": paths
    }
