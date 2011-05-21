from django.contrib import admin
from models import Praise

#class PageAdmin(TreeAdmin):
#    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Praise, admin.ModelAdmin)