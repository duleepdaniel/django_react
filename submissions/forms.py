from django import forms

class SubmissionForm(forms.Form):
    firstname = forms.CharField(label="Enter First name", max_length=100)
    lastname = forms.CharField(label="Enter Last name", max_length=100)
    age = forms.IntegerField(label="Enter Age")