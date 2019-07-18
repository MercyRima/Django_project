from django.contrib import admin

# Register your models here.

from.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display =("first_name","last_name","registration_number","date_joined","profile_picture")
	list_filter=("date_joined","date_of_birth")
admin.site.register(Student,StudentAdmin)
