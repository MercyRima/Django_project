from django.db import models

# Create your models here.

class Teacher(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	registration_number = models.CharField(max_length = 20)
	place_of_recidance = models.CharField(max_length = 20)
	phone_number = models.CharField(max_length = 16)
	email = models.EmailField(max_length = 70)
	id_number = models.IntegerField()
	date_employed = models.DateField()
	proffesional = models.CharField(max_length = 30)
	profile_picture = models.ImageField(upload_to="Teacher_image",blank=True,null=True)

	def __str__(self):
		return self.first_name+" "+self.last_name
		