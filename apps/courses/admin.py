from django.contrib import admin
from models import Course

#class EventAdmin(admin.ModelAdmin):

admin.site.register(Course, admin.ModelAdmin)