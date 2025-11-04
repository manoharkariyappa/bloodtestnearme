# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_offers(image=None, name=None, name1=None):
#     """
#     Query-based API for Offers.

#     - Without `image`: returns all active offers with name, image, and link.
#     - With `image`: returns only link(s) for that image.

#     -/api/method/bloodtestnearme.api.offers.get_offers
#     -/api/method/bloodtestnearme.api.offers.get_offers?image=example.jpg
#     """

#     if image:
#         # Return links for a specific image
#         query = """
#             SELECT link
#             FROM `tabOffers`
#             WHERE image = %s AND is_active = 1
#         """
#         result = frappe.db.sql(query, (image,), as_dict=True)
#         return [r["link"] for r in result]

#     query = """
#         SELECT
#             name,
#             name1,
#             image,
#             link
#         FROM `tabOffers`
#         WHERE is_active = 1
#         ORDER BY modified DESC
#     """
#     return frappe.db.sql(query, as_dict=True)

import frappe

@frappe.whitelist(allow_guest=True)
def get_offers(image=None, name=None, name1=None):
    """
    Fetch Offers

    - Optional filters: image, name (ID), name1 (Offer Name)
    - If parameters are provided, results are filtered accordingly.
    - Returns: id, name, image, link, and order_by fields.

    Examples:
      /api/method/bloodtestnearme.api.offers.get_offers
      /api/method/bloodtestnearme.api.offers.get_offers?image=/files/B_4.png
      /api/method/bloodtestnearme.api.offers.get_offers?name=gp2tb9sqic
      /api/method/bloodtestnearme.api.offers.get_offers?name1=blood%20test%20offer
    """

    conditions = ["is_active = 1"]
    values = []

    # Dynamically add filters
    if image:
        conditions.append("image = %s")
        values.append(image)
    if name:
        conditions.append("name = %s")
        values.append(name)
    if name1:
        conditions.append("name1 = %s")
        values.append(name1)

    where_clause = " AND ".join(conditions)

    query = f"""
        SELECT
            name,
            name1,
            image,
            link,
            description,
            order_by
        FROM `tabOffers`
        WHERE {where_clause}
        ORDER BY order_by ASC, modified DESC
    """

    offers = frappe.db.sql(query, tuple(values), as_dict=True)

    formatted_offers = [
        {
            "id": o["name"],
            "name": o["name1"],
            "image": o["image"],
            "link": o["link"],
            "description": o.get("description"),
            "order_by": o.get("order_by")
        }
        for o in offers
    ]

    return formatted_offers
