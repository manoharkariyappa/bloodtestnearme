import frappe

@frappe.whitelist(allow_guest=True)
def global_quick_search(query=None):
    if not query:
        return []

    query = query.strip().lower()
    results = []

    doctypes_config = {
        "Packages": [
            "name1", "url", "actual_price", "discounted_price", "package_name",
            "description", "list_include", "title"
        ],
        "Package Category": [
            "name1", "title", "description"
        ],
        # "Pincodes": [
        #     "name1", "pincode", "state", "district"
        # ],
        # "Family Health Package": ["name1", "description", "category"],
        # "Family Package Test": ["name1", "description"],
        # "Order": ["name1", "title", "description"],
        # "Related Package": ["name1", "description"],
        # "Testing Object": ["name1", "description", "list_include"]
    }

    for doctype, fields in doctypes_config.items():
        meta = frappe.get_meta(doctype)
        valid_fields = [f for f in fields if f in [d.fieldname for d in meta.fields]]

        if not valid_fields:
            continue

        conditions = " OR ".join([f"LOWER(`{field}`) LIKE %(q)s" for field in valid_fields])
        sql = f"""
            SELECT {', '.join([f'`{f}`' for f in valid_fields])}
            FROM `tab{doctype}`
            WHERE {conditions}
            LIMIT 10
        """

        try:
            records = frappe.db.sql(sql, {"q": f"%{query}%"}, as_dict=True)
            for rec in records:
                # Only include non-empty fields
                filtered = {k: v for k, v in rec.items() if v}
                if filtered:
                    results.append(filtered)
        except Exception as e:
            frappe.log_error(f"Error in global search ({doctype}): {e}")

    return results
