from django.test import TestCase
from.models import Course
import datetime
from.forms import CourseForm
from django.urls import reverse
from django.test import Client
client=Client()
class CreateCourseTestCase(TestCase):
    def setUp(self):
        self.data={
        "name":"python",
        "duration_in_months":4,
        "course_number":"667765",
        "description":"data"
        
    
        }
        self.bad_data={
            "name":987,
            "duration_in_months":"4",
            "course_number":"656677",
            'description':"data",
            "teacher":"James Mwai"
            }
    
    def test_course_form_always_valid_data(self):
        form=CourseForm(self.data)
        self.assertTrue(form.is_valid())
        
    def test_bad_course_form_reject_invalid_data(self):
        form=CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_course_view(self):
        url = reverse("add_course")
        request=client.post (url,self.data)
        self.assertEqual(request.status_code,200)

    def test_add_bad_view(self):
        url = reverse("add_course")
        request=client.post (url,self.bad_data)
        self.assertEqual(request.status_code,400)

    
# Create your tests here.
