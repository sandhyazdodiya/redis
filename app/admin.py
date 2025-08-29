from django.contrib import admin
from .models import User, Candidate, Company, Job, JobApplication, CandidateEducation, ApplicationFeedback, Offer, ActivityLogs
from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
# Register your models here.

admin.site.register(Permission)
admin.site.register(LogEntry)
admin.site.register(ContentType)
admin.site.register(Session)


@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    pass 

@admin.register(Candidate) 
class CandidateAdmin(admin.ModelAdmin):
    pass 

@admin.register(Job) 
class JobeAdmin(admin.ModelAdmin):
    pass 

@admin.register(JobApplication) 
class JobApplicationAdmin(admin.ModelAdmin):
    pass 

@admin.register(CandidateEducation) 
class CandidateEducationAdmin(admin.ModelAdmin):
    pass 

@admin.register(ApplicationFeedback) 
class ApplicationFeedbackAdmin(admin.ModelAdmin):
    pass 

@admin.register(Offer) 
class OfferAdmin(admin.ModelAdmin):
    pass 

@admin.register(ActivityLogs) 
class ActivityLogsAdmin(admin.ModelAdmin):
    pass 