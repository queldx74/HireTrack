from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "job_title",
            "company",
            "location",
            "date_applied",
            "status",
            "job_url",
            "salary",
            "notes",
        ]