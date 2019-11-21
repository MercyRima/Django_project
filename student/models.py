from django.db import models
from course.models import Course
from django.core.exceptions import ValidationError
import datetime 
# Create your models here.

class Student(models.Model):
	first_name= models.CharField(max_length = 50)
	last_name= models.CharField(max_length = 50)
	date_of_birth= models.DateField()
	registration_number= models.CharField(max_length = 30)
	place_of_recidance= models.CharField(max_length = 30)
	phone_number= models.CharField(max_length = 30)
	email= models.EmailField(max_length = 70)
	guardian_phone= models.CharField(max_length = 30)
	id_number= models.IntegerField()
	date_joined= models.DateField()
	course=models.ManyToManyField(Course,null=True,blank=True,related_name="Students")
	profile_picture= models.ImageField(upload_to="Student_image",null=True, blank=True)
	
	
	def __str__(self):
		return self.first_name+" "+self.last_name

	def full_name(self):
		return "{} {}".format(self.first_name,self.last_name)
	def get_age(self):
		today = datetime.date.today()
		return today.year - self.date_of_birth.year
	age = property(get_age)
	def clean(self):
		age = self.age
		if age <18 or age>30:
			raise ValidationError("Only above 17 years and Above 30 years")
		return age

	def teachers(self):
		return[course.teacher for course in self.courses.all()]

	