import frappe

@frappe.whitelist(allow_guest=True)
def get_active_package_categories(url=None):
    """
    Return all active package categories.
    If `url` parameter is passed, return only that specific category.
    """

    if url:
        query = """
            SELECT
                name,
                name1,
                title,
                url,
                description,
                image,
                is_active
            FROM
                `tabPackage Category`
            WHERE
                is_active = 1
                AND url = %s
            ORDER BY modified DESC
        """
        data = frappe.db.sql(query, (url,), as_dict=True)

    else:
        # Fetch all active categories
        query = """
            SELECT
                name,
                name1,
                title,
                url,
                description,
                image,
                is_active
            FROM
                `tabPackage Category`
            WHERE
                is_active = 1
            ORDER BY modified DESC
        """
        data = frappe.db.sql(query, as_dict=True)

    return {"status": "success", "data": data}
