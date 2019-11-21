from django.test import TestCase
from course.models import Course
from teacher.models import Teacher
import datetime
class CourseTeacherTestCase(TestCase):
    def setUp(self):
        self.teacher_a=Teacher.objects.create(
            first_name="Kelly",
            last_name="Gatwiri",
            registration_number="6673765",
            place_of_recidance="Westlands",
            phone_number="076536773",
            email="Kelly@gmail.com",
            id_number=98774647787,
            date_employed=datetime.date.today(),
            proffesional="Entreprenur",)
        self.teacher_b=Teacher.objects.create(
            first_name="James",
            last_name="Mwai",
            registration_number="6673765",
            place_of_recidance="Westlands",
            phone_number="076536773",
            email="mwai@gmail.com",
            id_number=98774647787,
            date_employed=datetime.date.today(),
            proffesional="Developer",
            )
        self.python=Course.objects.create(
            name="python",
            duration_in_months=10,
            course_number="1",
            description="Learn Python",
            )

        self.javascript=Course.objects.create(
            name="javascript",
            duration_in_months=10,
            course_number="2",
            description="Learn JS",)

        self.hardware=Course.objects.create(
            name="hardware",
            duration_in_months=10,
            course_number="3",
            description="Build hardware",)

    def test_teacher_can_have_many_courses(self):
        self.assertEqual(self.teacher_a.courses.count(),0)
        self.teacher_a.course.add(self.python)
        self.assertEqual(self.teacher_a.courses.count(),1)
        self.teacher_a.course.add(self.javascript)
        self.assertEqual(self.teacher_a.course.count(),2)
        self.teacher_a.course.add(self.hardware)
        self.assertEqual(self.teacher_a.course.count(),3)

    def test_course_can_only_have_one_teacher(self):
      self.python.teacher=self.teacher_a
      self.assertEqual(self.python.teacher.first_name,"Kelly")
      self.python.teacher=self.teacher_b
      self.assertEqual(self.python.teacher.first_name,"James")
