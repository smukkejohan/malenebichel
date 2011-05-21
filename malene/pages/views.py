from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from models import Page

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})

def legacy_page_detail(request, parent_slug, child_slug):
    """
    Redirect old urls in the /parent-slug/child-slug/$ format to new
    url scheme /page-slug/$
    """

    page = get_object_or_404(Page, slug=child_slug)

    return HttpResponseRedirect(page.get_absolute_url())