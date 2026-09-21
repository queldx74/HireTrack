from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobApplication
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

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

class EmailUpdateForm(forms.Form):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "autocomplete": "email",
            }
        ),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if user and not self.is_bound:
            self.fields["email"].initial = user.email

    def clean_email(self):
        email = self.cleaned_data["email"].strip()

        # Prevent another account from already using this email.
        if self.user:
            UserModel = self.user.__class__

            if (
                UserModel.objects
                .exclude(pk=self.user.pk)
                .filter(email__iexact=email)
                .exists()
            ):
                raise forms.ValidationError(
                    "An account with this email address already exists."
                )

        return email


class AccountPasswordChangeForm(forms.Form):
    current_password = forms.CharField(
        label="Current password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
            }
        ),
    )

    new_password1 = forms.CharField(
        label="New password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
            }
        ),
    )

    new_password2 = forms.CharField(
        label="Confirm new password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
            }
        ),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_current_password(self):
        password = self.cleaned_data["current_password"]

        if not self.user or not self.user.check_password(password):
            raise forms.ValidationError("Your current password is incorrect.")

        return password

    def clean(self):
        cleaned_data = super().clean()

        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                self.add_error(
                    "new_password2",
                    "The new passwords do not match.",
                )
            else:
                try:
                    password_validation.validate_password(
                        new_password1,
                        self.user,
                    )
                except ValidationError as error:
                    self.add_error("new_password1", error)

        return cleaned_data


class DeleteAccountForm(forms.Form):
    current_password = forms.CharField(
        label="Current password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
            }
        ),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_current_password(self):
        password = self.cleaned_data["current_password"]

        if not self.user or not self.user.check_password(password):
            raise forms.ValidationError("Your current password is incorrect.")

        return password

    