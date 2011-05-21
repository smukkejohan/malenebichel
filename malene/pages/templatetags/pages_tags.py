import pprint
from django import template
from pages.models import Page

register = template.Library()

@register.inclusion_tag('_page_navigation.html', takes_context = True)
def render_page_navigation(context):
    """
    Render hierarchical page navigation

    """

    current_page = None
    parent_page = None

    try:
        # Get the current page object if we are on a detail view
        current_page = context['page']
        parent_page = current_page.get_parent()
        print parent_page
    except KeyError:
        pass

    annotated_pages = Page.get_annotated_list()

    return {'annotated_pages': annotated_pages,
        'current_page': current_page,
        'parent_page': parent_page, }