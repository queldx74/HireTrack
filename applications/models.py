from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

	STATUS_CHOICES = [
		("saved", "Saved"),
		("applied", "Applied"),
		("interview", "Interview"),
		("offer", "Offer"),
		("rejected", "Rejected"),
		("withdrawn", "Withdrawn"),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	job_title = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	location = models.CharField(max_length=200, blank=True)
	date_applied = models.DateField()
	status = models.CharField(
		max_length=20,
		choices=STATUS_CHOICES,
		default="saved"
	)
	job_url = models.URLField(blank=True)
	salary = models.CharField(max_length=100, blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return f"{self.job_title} at {self.company}"
