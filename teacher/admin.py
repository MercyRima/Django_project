from django.contrib import admin

# Register your models here.

from.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
	list_display =("first_name","last_name","registration_number","email")
admin.site.register(Teacher,TeacherAdmin)
