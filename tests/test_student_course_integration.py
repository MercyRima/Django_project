from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime

class StudentCourseTestCase(TestCase):
    def setUp(self):

         self.student_a=Student.objects.create(
            first_name="mercy",
            last_name="rima",
            date_of_birth=datetime.date(2000,8,13),
            registration_number="662387876",
            place_of_recidance="Kilimani",
            email="macrimah60@gmail.com",
            phone_number="07345442323",
            guardian_phone="09878654",
            id_number=765456,
            date_joined=datetime.date.today(),
)



         self.student_b=Student.objects.create(
            first_name="mary",
            last_name="wanja",
            date_of_birth=datetime.date(2000,8,13),
            registration_number="645383939",
            place_of_recidance="kabete",
            email="marywanja78@gmail.com",
            phone_number="07345653443",
            guardian_phone="07654422",
            id_number=36582706,
            date_joined=datetime.date.today(),
)

        
         self.python=Course.objects.create(
            name="python",
            duration_in_months=4,
            course_number="6664433345",
            description="My day swwswvhj"
        
    
        )



         self.javascript=Course.objects.create(
            name="Es",
            duration_in_months=6,
            course_number="66655445",
            description="Type something"
        
    
        )


       
         self.hardware=Course.objects.create(
            name="hardware",
            duration_in_months=7,
            course_number="7645445",
            description="Lorem ipsum"
        
    
        )


         self.teacher=Teacher.objects.create(
            first_name="Kelly",
            last_name="Gatwiri",
            registration_number="6673765",
            place_of_recidance="Westlands",
            phone_number="076536773",
            email="Kelly@gmail.com",
            id_number=98774647787,
            date_employed=datetime.date.today(),
            proffesional="Entreprenur",
        )


    def test_student_can_join_many_courses(self):
        self.assertEqual(self.student_a.course.count(),0)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.course.count(),1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.course.count(),2)
        self.student_a.courses.add(self.hardware)
        self.assertEqual(self.student_a.course.count(),3)



    def test_course_can_have_many_students(self):
        self.python.students.add(self.student_a, self.student_b)
        self.assertEqual(self.python.students.count(), 2)


    def test_teacher_can_teach_many_courses(self):
        self.teacher_a.courses.add(self.hardware,self.python,self.javascript)
        self.assertEqual(self.teacher_a.courses.count(),3)


    def test_course_can_have_only_one_teacher(self):
        self.python.teacher= self.teacher_a
        self.assertEqual(self.python.teacher.first_name, "James")
        self.javascript.teacher = self.teacher_b
        self.assertEqual(self.javascript.teacher.first_name, "Antony")


    def test_course_teacher_is_in_student_teachers_list(self):
        self.python.teacher=self.teacher_b
        self.student_a.courses.add(self.python)
        teachers=self.student_a.teachers
        self.assertTrue(self.teacher_b in teachers)







        

    # def test_course_can_have_many_students(self):
    #     self.python.students.add(self.student_a,self.student_b)
    #     self.assertEqual(self.python.students.count(),2)

   


    # def test_course_teacher_is_in_student_teachers_list(self):
    #     self.python.teacher=self.teacher_b
    #     self.student_a.courses.add(self.python)
    #     teachers=self.student_a.teachers
    #     self.assertTrue(self.teacher_b in teachers)



    # def test_course_teacher_is_in_student_teachers_list(self):

    # def test_can_have_many_course

    # def test_course_cannot_have_many_teachers

