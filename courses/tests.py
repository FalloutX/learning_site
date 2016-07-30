from django.test import TestCase
from django.utils import timezone
from .models import Course, Step

# Create your tests here.

class CourseModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in Python."
        )

    def test_course_creation(self):
        now = timezone.now()
        self.assertLess(self.course.created_at, now)

    def test_step_creation(self):
        step = Step.objects.create(
            title="Introduction to Docsets",
            description="Learn to write Tests in your docstrings",
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())
