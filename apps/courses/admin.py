from django.contrib import admin
from models import Course, Signup

class CourseAdmin(admin.ModelAdmin):
    list_display  = ('title', 'custom_time', 'start_date', 'end_date', 'status', 'signup_open')
    list_filter   = ('start_date', 'end_date', 'status', 'signup_open')
    search_fields = ('title', 'description', 'location', 'body')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'description', 'body', 'location', 'price', 'status', 'display_frontpage')
        }),
        ('Tid og dato', {
           'fields': ('custom_time', 'start_date', 'end_date'),
        }),
        ('Tilmelding', {
           'fields': ('signup_open', 'signup_link',),
           'classes': ('collapse',)
        }),
    )

admin.site.register(Course, CourseAdmin)


class SignupAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'email', 'phone', 'course', 'time')
    list_filter   = ('time', 'course',)
    search_fields = ('first_name', 'last_name', 'note')


admin.site.register(Signup, SignupAdmin)