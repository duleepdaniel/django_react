from django.urls import path
from . import views

urlpatterns = [
    path('submissions/', views.submissions, name='submissions'),
    path('submissions/create_submission', views.create_submission, name='create_submissions'),
]