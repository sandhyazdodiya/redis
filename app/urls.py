from django.urls import path
from .views import (
    UserAPIView, CandidateAPIView, CandidateEducationAPIView, CompanyAPIView,
    JobAPIView, JobApplicationAPIView, ApplicationFeedbackAPIView, OfferAPIView,
    ActivityLogsAPIView, RegisterView, LoginView
)

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),
    path('candidates/', CandidateAPIView.as_view()),
    path('candidates/<int:pk>/', CandidateAPIView.as_view()),
    path('candidate-educations/', CandidateEducationAPIView.as_view()),
    path('candidate-educations/<int:pk>/', CandidateEducationAPIView.as_view()),
    path('companies/', CompanyAPIView.as_view()),
    path('companies/<int:pk>/', CompanyAPIView.as_view()),
    path('jobs/', JobAPIView.as_view()),
    path('jobs/<int:pk>/', JobAPIView.as_view()),
    path('job-applications/', JobApplicationAPIView.as_view()),
    path('job-applications/<int:pk>/', JobApplicationAPIView.as_view()),
    path('application-feedbacks/', ApplicationFeedbackAPIView.as_view()),
    path('application-feedbacks/<int:pk>/', ApplicationFeedbackAPIView.as_view()),
    path('offers/', OfferAPIView.as_view()),
    path('offers/<int:pk>/', OfferAPIView.as_view()),
    path('activity-logs/', ActivityLogsAPIView.as_view()),
    path('activity-logs/<int:pk>/', ActivityLogsAPIView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')]
    