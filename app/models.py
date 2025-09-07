# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings     


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    user_role = models.CharField(max_length=9, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'


class Candidate(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    resume_url = models.CharField(max_length=1000, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'candidate'


class CandidateEducation(models.Model):
    id = models.IntegerField(primary_key=True)
    candidate = models.ForeignKey(Candidate, models.DO_NOTHING)
    degree = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_year = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'candidate_education'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    comapny_name = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'company'


class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    job_description = models.CharField(max_length=1000, blank=True, null=True)
    job_type = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary_min = models.IntegerField(blank=True, null=True)
    salary_max = models.IntegerField(blank=True, null=True)
    skills_required = models.JSONField(blank=True, null=True)
    job_status = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'job'


class JobApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.ForeignKey(Job, models.DO_NOTHING, blank=True, null=True)
    candidate = models.ForeignKey(Candidate, models.DO_NOTHING, blank=True, null=True)
    application_status = models.CharField(max_length=9, blank=True, null=True)
    applied_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'job_application'

class ApplicationFeedback(models.Model):
    id = models.IntegerField(primary_key=True)
    application = models.ForeignKey('JobApplication', models.DO_NOTHING, blank=True, null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    round_name = models.CharField(max_length=17, blank=True, null=True)
    feedback = models.JSONField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'application_feedback'


class Offer(models.Model):
    id = models.IntegerField(primary_key=True)
    application = models.ForeignKey(JobApplication, models.DO_NOTHING, blank=True, null=True)
    offered_salary = models.IntegerField(blank=True, null=True)
    joining_date = models.CharField(max_length=255, blank=True, null=True)
    application_status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'offer'


class ActivityLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    action_state = models.CharField(max_length=255, blank=True, null=True)
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    entity_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activity_logs'



