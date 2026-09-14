from django.test import TestCase
from django.contrib.auth.models import User
from .models import JobApplication


class JobApplicationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.application = JobApplication.objects.create(
            user=self.user,
            job_title="Software Developer",
            company="Test Company",
            date_applied="2026-09-14",
            status="applied",
        )

    def test_application_created(self):
        self.assertEqual(
            self.application.company,
            "Test Company"
        )

    def test_application_belongs_to_user(self):
        self.assertEqual(
            self.application.user,
            self.user
        )