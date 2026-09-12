from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        widgets = {
            "job_title": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "e.g. Product Designer"
            }),
            "company": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "e.g. Nova Studio"
            }),
            "location": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "e.g. Remote, Edinburgh"
            }),
            "date_applied": forms.DateInput(attrs={
                "class": "form-control", "type": "date"
            }),
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
            "job_url": forms.URLInput(attrs={
                "class": "form-control", "placeholder": "https://"
            }),
            "salary": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "e.g. £45,000"
            }),
            "notes": forms.Textarea(attrs={
                "class": "form-control", "rows": 4,
                "placeholder": "Contacts, interview prep, follow-up reminders…"
            }),
        }
        labels = {
            "job_title": "Job title",
            "job_url": "Job posting link",
            "date_applied": "Date applied",
        }


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="Full name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Jordan Smith"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "jordan@email.com"})
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "jordansmith"})
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "At least 8 characters"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Re-enter your password"})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        return user