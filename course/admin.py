from django.contrib import admin

# Register your models here
from.models import Course


class CourseAdmin(admin.ModelAdmin):
	list_display =("name", "description","course_number","teacher")
	search_fields =("course_number","teacher__email","teacher__registration_number")
	list_filter = ("teacher__first_name",)
admin.site.register(Course,CourseAdmin)
