import frappe

@frappe.whitelist(allow_guest=True)
def get_blogs():
    blogs = frappe.get_all(
        "Blogs",
        fields=[
            "name",
            "header_image",
            "thumbnail_image", 
            "description_heading_1",
            "description_1",
            "description_heading_2",
            "description_2",
            "description_heading_3",
            "description_3",
            "description_heading_4",
            "description_4",
            "blog_date",
            "sub_description_heading_1",
            "sub_description_heading_2",
            "sub_description_heading_3",
            "sub_description_heading_4",
            "custom_html"
        ],
        order_by="creation desc"
    )

    # Add full URL for images
    for blog in blogs:
        if blog.get("header_image"):
            blog["header_image"] = frappe.utils.get_url(blog["header_image"])
        if blog.get("thumbnail_image"):
            blog["thumbnail_image"] = frappe.utils.get_url(blog["thumbnail_image"])

    return blogs


@frappe.whitelist(allow_guest=True)
def get_blog(blog_name):
    """
    Fetch a single Education-Blog by name
    """
    try:
        blog = frappe.get_doc("Blogs", blog_name)
        # Convert image fields to full URLs
        if blog.header_image:
            blog.header_image = frappe.utils.get_url(blog.header_image)
        if blog.thumbnail_image:
            blog.thumbnail_image = frappe.utils.get_url(blog.thumbnail_image)

        return {
            "name": blog.name,
            "header_image": blog.header_image,
            "thumbnail_image": blog.thumbnail_image,
            "description_heading_1": blog.description_heading_1,
            "description_1": blog.description_1,
            "description_heading_2": blog.description_heading_2,
            "description_2": blog.description_2,
            "description_heading_3": blog.description_heading_3,
            "description_3": blog.description_3,
            "description_heading_4": blog.description_heading_4,
            "description_4": blog.description_4,
            "custom_html": blog.custom_html
        }
    except frappe.DoesNotExistError:
        return {}
