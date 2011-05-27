from treebeard.admin import TreeAdmin
from django.contrib import admin
from models import Page

class PageAdmin(TreeAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)