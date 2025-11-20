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
        ]
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
            LIMIT 50
        """

        try:
            records = frappe.db.sql(sql, {"q": f"%{query}%"}, as_dict=True)
            for rec in records:
                filtered = {k: v for k, v in rec.items() if v}
                if filtered:
                    results.append(filtered)
        except Exception as e:
            frappe.log_error(f"Error in global search ({doctype}): {e}")


    def sort_priority(item):
        for v in item.values():
            text = str(v).lower()
            if text.startswith(query):
                return 0  
            if query in text:
                return 1
        return 2

    results = sorted(results, key=sort_priority)

    return results
