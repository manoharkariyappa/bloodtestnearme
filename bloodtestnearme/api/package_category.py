import frappe


@frappe.whitelist(allow_guest=True)
def get_active_package_categories():
    """
    Return all active and submitted Package Categories
    (is_active = 1)
    """
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
        ORDER BY
            modified DESC
    """
    data = frappe.db.sql(query, as_dict=True)
    return {"status": "success", "data": data}
