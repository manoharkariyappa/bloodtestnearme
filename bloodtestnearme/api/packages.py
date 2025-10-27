import frappe

@frappe.whitelist(allow_guest=True)
def get_all_packages():
    """Fetch all active packages"""
    packages = frappe.get_all(
        "Packages",
        fields=[
            "name1",
            "image",
            "package_name",
            "category",
            "testing_type",
            "actual_price",
            "discounted_price",
            "number_of_test",
            "description",
            "list_include",
            "in_house",
            "fasting_required",
            "is_active",
            "reference_link",
            "url",
            "meta_description",
            "meta_keyword",
            "header_tag"
        ],
        filters={"is_active": 1},
        order_by="order_sequence asc"
    )
    return packages


@frappe.whitelist(allow_guest=True)
def get_packages_by_category(category):
    """Fetch all active packages under a specific category"""
    if not category:
        frappe.throw("Category is required")

    packages = frappe.get_all(
        "Packages",
        fields=[
            "name1",
            "image",
            "package_name",
            "category",
            "testing_type",
            "actual_price",
            "discounted_price",
            "number_of_test",
            "description",
            "list_include",
            "in_house",
            "fasting_required",
            "is_active",
            "reference_link",
            "url"
        ],
        filters={"category": category, "is_active": 1},
        order_by="order_sequence asc"
    )
    return packages

@frappe.whitelist(allow_guest=True)
def get_packages(category=None, package_name=None):
    """
    Public API to fetch packages.
    
    - If no params: returns all active packages.
    - If `category` or `testing_type` is provided: filters results accordingly.
    
    Example:
        /api/method/bloodtestnearme.api.packages.get_packages
        /api/method/bloodtestnearme.api.packages.get_packages?category=Male
        /api/method/bloodtestnearme.api.packages.get_packages?package_name=Packages
    """
    try:
        filters = {"is_active": 1}
        if category:
            filters["category"] = category
        if package_name:
            filters["package_name"] = package_name

        packages = frappe.get_all(
            "Packages",
            filters=filters,
            fields=[
                "name1",
                "image",
                "category",
                "testing_type",
                "actual_price",
                "discounted_price",
                "number_of_test",
                "package_name",
                "description",
                "sample_type",
                "in_house",
                "fasting_required",
                "url",
                "doctor_consultation",
                "meta_description",
                "meta_keyword",
                "header_tag",
                "list_include",
                "booking_procedure"
            ],
            order_by="order_sequence asc"
        )

        return {
            "status": "success",
            "count": len(packages),
            "data": packages
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Get Packages API Error")
        return {
            "status": "error",
            "message": str(e)
        }

@frappe.whitelist(allow_guest=True)
def get_package_by_name(package_name):
    """Fetch a single package by its name"""
    if not package_name:
        frappe.throw("Package Name is required")

    package = frappe.get_all(
        "Packages",
        fields=["*"],
        filters={"package_name": package_name, "is_active": 1},
        limit_page_length=1
    )

    if not package:
        frappe.throw(f"No package found with name {package_name}")

    # get_all returns a list, return the first record
    return package[0]


@frappe.whitelist(allow_guest=True)
def get_most_booking_packages():
    """Return list of packages tagged as 'mostbooked' and active"""
    data = frappe.get_all(
        "Packages",
        filters={
            "is_active": 1
        },
        fields=[
            "name as id",
            "name1 as name",
            "package_name",
            "actual_price",
            "discounted_price",
            "url",
            "image",
            # "tags"
        ]
    )

    related_packages = [
        pkg for pkg in data
        if pkg.get("tags") and "mostbooked" in pkg["tags"].lower()
    ]

    return related_packages


@frappe.whitelist(allow_guest=True)
def get_most_booking_tests():
    """Return list of tests tagged as 'mostbooktests' and active"""
    data = frappe.get_all(
        "Packages",
        filters={
            "is_active": 1
        },
        fields=[
            "name as id",
            "name1 as name",
            "package_name",
            "actual_price",
            "discounted_price",
            "url",
            "image",
            # "tags"
        ]
    )

    related_tests = [
        pkg for pkg in data
        if pkg.get("tags") and "mostbooktests" in pkg["tags"].lower()
    ]

    return related_tests
