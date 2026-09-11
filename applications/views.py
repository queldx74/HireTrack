from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobApplicationForm


@login_required
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return redirect("dashboard")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "applications/add_application.html",
        {"form": form},
    )





from django.shortcuts import get_object_or_404


@login_required
def edit_application(request, application_id):

    application = get_object_or_404(
        JobApplication,
        id=application_id,
        user=request.user,
    )

    if request.method == "POST":
        form = JobApplicationForm(
            request.POST,
            instance=application,
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        "applications/edit_application.html",
        {
            "form": form,
            "application": application,
        },
    )