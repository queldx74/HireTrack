from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, JobApplicationForm
from .models import JobApplication


def home(request):
    return render(request, "application/home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/registration.html", {"form": form})


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user).order_by("-date_applied")

    context = {
        "applications": applications,
        "total": applications.count(),
        "applied_count": applications.filter(status="applied").count(),
        "interview_count": applications.filter(status="interview").count(),
        "offer_count": applications.filter(status="offer").count(),
        "rejected_count": applications.filter(status="rejected").count(),
    }
    return render(request, "application/dashboard.html", context)


@login_required
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Application added.")
            return redirect("dashboard")
    else:
        form = JobApplicationForm()

    return render(request, "application/add-application.html", {"form": form})


@login_required
def application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    return render(request, "application/application-details.html", {"application": application})


@login_required
def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Application updated.")
            return redirect("application_detail", pk=application.pk)
    else:
        form = JobApplicationForm(instance=application)

    return render(request, "application/edit-application.html", {"form": form, "application": application})


@login_required
def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == "POST":
        application.delete()
        messages.success(request, "Application deleted.")
        return redirect("dashboard")

    return render(request, "application/delete-confirmation.html", {"application": application})

@login_required

def statistics(request):
    applications = JobApplication.objects.filter(user=request.user)

    status_counts = []
    for status_code, status_label in JobApplication.STATUS_CHOICES:
        status_counts.append({
            "code": status_code,
            "label": status_label,
            "count": applications.filter(status=status_code).count(),
        })

    valid_status_codes = [code for code, label in JobApplication.STATUS_CHOICES]
    selected_status = request.GET.get("status", "all")

    if selected_status != "all" and selected_status not in valid_status_codes:
        selected_status = "all"

    if selected_status == "all":
        filtered_applications = applications.order_by("-date_applied")
    else:
        filtered_applications = applications.filter(status=selected_status).order_by("-date_applied")

    context = {
        "total": applications.count(),
        "status_counts": status_counts,
        "selected_status": selected_status,
        "filtered_applications": filtered_applications,
    }
    return render(request, "application/statistics.html", context)

# Custom error handlers

def error_403(request, exception):
    return render(request, "error/403.html", status=403)


def error_404(request, exception):
    return render(request, "error/404.html", status=404)


def error_500(request):
    return render(request, "error/500.html", status=500)


@login_required
def dashboard(request):
    status_filter = request.GET.get('status')
    
    # Keep your existing user-ownership security
    applications = JobApplication.objects.filter(user=request.user)
    
    # Filter by status if query parameter is present in URL
    if status_filter:
        applications = applications.filter(status__iexact=status_filter)
        
    context = {
        'applications': applications,
        'total': JobApplication.objects.filter(user=request.user).count(),
        'applied_count': JobApplication.objects.filter(user=request.user, status__iexact='applied').count(),
        'interview_count': JobApplication.objects.filter(user=request.user, status__iexact='interview').count(),
        'offer_count': JobApplication.objects.filter(user=request.user, status__iexact='offer').count(),
    }
    
    return render(request, 'application/dashboard.html', context)