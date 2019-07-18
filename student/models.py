from django.db import models
from course.models import Course

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()
	registration_number = models.CharField(max_length = 20)
	place_of_recidance = models.CharField(max_length = 20)
	phone_number = models.CharField(max_length = 16)
	email = models.EmailField(max_length = 70)
	guardian_phone = models.CharField(max_length = 16)
	id_number = models.IntegerField()
	date_joined = models.DateField()
	course=models.ManyToManyField(Course)
	profile_picture = models.ImageField(upload_to="Student_image",blank=True,null=True)

	course = models.ManyToManyField(Course)