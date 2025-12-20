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
            "title",
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
def get_packages(category=None, package_name=None, url=None):
    """
    Public API to fetch packages.
    
    - If no params: returns all active packages.
    - If `category` or `testing_type` is provided: filters results accordingly.
    
    Example:
        /api/method/bloodtestnearme.api.packages.get_packages
        /api/method/bloodtestnearme.api.packages.get_packages?category=Male
        /api/method/bloodtestnearme.api.packages.get_packages?package_name=Packages
        /api/method/bloodtestnearme.api.packages.get_packages?url=exampleurl
    """
    try:
        filters = {"is_active": 1}
        if category:
            filters["category"] = category
        if package_name:
            filters["name1"] = package_name
        if url:
            filters["url"] = url

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
                "title",
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
             "tags",
             "title"
        ]
    )

    related_packages = [
        pkg for pkg in data
        if pkg.get("tags") and "mostbooked" in pkg["tags"].lower()
    ]

    return related_packages

@frappe.whitelist(allow_guest=True)
def get_packages_by_tags(tag=None):
    if not tag:
        return {"error": "tag parameter is required"}

    # 1 Get all parent package names that match the tag
    package_names = frappe.db.get_all(
        "Packages Tags Group",
        filters={"tags": tag},
        fields=["parent"]
    )

    if not package_names:
        return []

    parents = [d.parent for d in package_names]

    # 2 Fetch required package fields
    packages = frappe.db.get_all(
        "Packages",
        filters={"name": ["in", parents], "is_active": 1},
        fields=[
            "name as id",
            "name1 as name",
            "package_name",
            "actual_price",
            "discounted_price",
            "url",
            "image",
            "title",
            "order_sequence"
        ],
         order_by="order_sequence asc"
    )

    # 3 Attach tag list to each package
    for pkg in packages:
        tags = frappe.db.get_all(
            "Packages Tags Group",
            filters={"parent": pkg["id"]},
            fields=["tags"]
        )
        pkg["tags"] = [t["tags"] for t in tags]

    return packages




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
            "tags",
            "title"
        ]
    )

    related_tests = [
        pkg for pkg in data
        if pkg.get("tags") and "mostbooktests" in pkg["tags"].lower()
    ]

    return related_tests

@frappe.whitelist(allow_guest=True)
def get_herosection_packages():
    """Return list of packages tagged as 'herosection' and active"""
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
             "tags",
             "title"
        ]
    )

    related_packages = [
        pkg for pkg in data
        if pkg.get("tags") and "herosection" in pkg["tags"].lower()
    ]

    return related_packages

@frappe.whitelist(allow_guest=True)
def get_individual_packages():
    """
    Fetch all active packages where Testing Type = 'Individual'
    
    Example:
        /api/method/bloodtestnearme.api.packages.get_individual_packages
    """
    try:
        packages = frappe.get_all(
            "Packages",
            filters={
                "is_active": 1,
                "testing_type": "Individual"
            },
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
                "title",
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
        frappe.log_error(frappe.get_traceback(), "Get Individual Packages API Error")
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=True)
def get_package_based_tests():
    """
    Fetch all active packages where Testing Type = 'Packages'
    
    Example:
        /api/method/bloodtestnearme.api.packages.get_package_based_tests
    """
    try:
        packages = frappe.get_all(
            "Packages",
            filters={
                "is_active": 1,
                "testing_type": "Packages"
            },
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
                "title",
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
        frappe.log_error(frappe.get_traceback(), "Get Package-based Tests API Error")
        return {"status": "error", "message": str(e)}
    
# 