from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SubmissionForm

def submissions(request):
    template = loader.get_template('submissions.html')
    return HttpResponse(template.render())


def create_submission(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            return redirect("/submissions/")
    else:
        form = SubmissionForm()

    return render(request, "create_submission.html", {"form": form})