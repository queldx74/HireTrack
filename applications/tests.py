from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
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


class StatisticsViewTests(TestCase):

    def setUp(self):
        # Two separate users, so we can test data isolation between them
        self.user_a = User.objects.create_user(username="usera", password="testpass123")
        self.user_b = User.objects.create_user(username="userb", password="testpass123")

        # User A: 2 saved, 1 applied, 1 interview, 0 of everything else
        JobApplication.objects.create(
            user=self.user_a, job_title="Designer", company="Nova",
            date_applied="2026-01-01", status="saved"
        )
        JobApplication.objects.create(
            user=self.user_a, job_title="Engineer", company="Atlas",
            date_applied="2026-01-02", status="saved"
        )
        JobApplication.objects.create(
            user=self.user_a, job_title="Analyst", company="Brightline",
            date_applied="2026-01-03", status="applied"
        )
        JobApplication.objects.create(
            user=self.user_a, job_title="Manager", company="Coastline",
            date_applied="2026-01-04", status="interview"
        )

        # User B: 1 interview application — used to test cross-user privacy
        JobApplication.objects.create(
            user=self.user_b, job_title="Consultant", company="Meridian",
            date_applied="2026-01-05", status="interview"
        )

        self.stats_url = reverse("statistics")

    # ---------- Access control ----------

    def test_statistics_requires_login(self):
        """An anonymous user should be redirected to login, not shown the page."""
        response = self.client.get(self.stats_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_statistics_loads_for_logged_in_user(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url)
        self.assertEqual(response.status_code, 200)

    # ---------- Counts (must reflect all of the user's applications) ----------

    def test_total_and_status_counts_are_correct(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url)

        self.assertEqual(response.context["total"], 4)

        counts = {item["code"]: item["count"] for item in response.context["status_counts"]}
        self.assertEqual(counts["saved"], 2)
        self.assertEqual(counts["applied"], 1)
        self.assertEqual(counts["interview"], 1)
        self.assertEqual(counts["offer"], 0)
        self.assertEqual(counts["rejected"], 0)
        self.assertEqual(counts["withdrawn"], 0)

    def test_counts_do_not_change_when_a_filter_is_applied(self):
        """Selecting a filter must not alter the top-level numbers — only the list below."""
        self.client.login(username="usera", password="testpass123")

        unfiltered = self.client.get(self.stats_url)
        filtered = self.client.get(self.stats_url, {"status": "interview"})

        self.assertEqual(unfiltered.context["total"], filtered.context["total"])
        self.assertEqual(
            unfiltered.context["status_counts"],
            filtered.context["status_counts"],
        )

    # ---------- Filtering behaviour ----------

    def test_no_filter_shows_all_applications(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url)

        self.assertEqual(response.context["selected_status"], "all")
        self.assertEqual(response.context["filtered_applications"].count(), 4)

    def test_filter_by_saved_returns_only_saved(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url, {"status": "saved"})

        self.assertEqual(response.context["selected_status"], "saved")
        results = response.context["filtered_applications"]
        self.assertEqual(results.count(), 2)
        self.assertTrue(all(app.status == "saved" for app in results))

    def test_filter_by_interview_returns_only_interview(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url, {"status": "interview"})

        results = response.context["filtered_applications"]
        self.assertEqual(results.count(), 1)
        self.assertEqual(results.first().job_title, "Manager")

    def test_filter_with_zero_matches_returns_empty_queryset_not_error(self):
        """User A has zero 'offer' applications — should return cleanly, not crash."""
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url, {"status": "offer"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["filtered_applications"].count(), 0)

    # ---------- Validation ----------

    def test_invalid_status_falls_back_to_all(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url, {"status": "banana"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["selected_status"], "all")
        self.assertEqual(response.context["filtered_applications"].count(), 4)

    def test_empty_status_param_falls_back_to_all(self):
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url, {"status": ""})

        self.assertEqual(response.context["selected_status"], "all")

    # ---------- Privacy: the most important test in this file ----------

    def test_statistics_only_includes_own_applications(self):
        """User A's stats/list must never include User B's data, filtered or not."""
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url)

        self.assertEqual(response.context["total"], 4)  # not 5
        for app in response.context["filtered_applications"]:
            self.assertEqual(app.user, self.user_a)

    def test_filter_cannot_leak_another_users_applications(self):
        """
        Both users have an 'interview' application. Filtering by ?status=interview
        as User A must return only User A's interview application, never User B's.
        """
        self.client.login(username="usera", password="testpass123")
        response = self.client.get(self.stats_url, {"status": "interview"})

        results = response.context["filtered_applications"]
        self.assertEqual(results.count(), 1)
        self.assertEqual(results.first().company, "Coastline")  # User A's, not Meridian (User B's)

        for app in results:
            self.assertEqual(app.user, self.user_a)

    def test_user_b_sees_only_their_own_data(self):
        self.client.login(username="userb", password="testpass123")
        response = self.client.get(self.stats_url)

        self.assertEqual(response.context["total"], 1)
        self.assertEqual(response.context["filtered_applications"].count(), 1)
        self.assertEqual(response.context["filtered_applications"].first().company, "Meridian")