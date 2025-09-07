from rest_framework import serializers
from .models import (
    User, Candidate, CandidateEducation, Company, Job,
    JobApplication, ApplicationFeedback, Offer, ActivityLogs
)

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    user_role = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    created_at = serializers.DateTimeField(allow_null=True, required=False)
    updated_at = serializers.DateTimeField(allow_null=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class CandidateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    candidate = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    dob = serializers.DateField(allow_null=True, required=False)
    gender = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    address = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    resume_url = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    experience = serializers.IntegerField(allow_null=True, required=False)
    skills = serializers.JSONField(allow_null=True, required=False)
    education = serializers.CharField(allow_blank=True, allow_null=True, required=False)

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class CandidateEducationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    degree = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    university = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    start_year = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    end_year = serializers.CharField(allow_blank=True, allow_null=True, required=False)

    def create(self, validated_data):
        return CandidateEducation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    comapny_name = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    company_description = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    website = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    industry = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    size = serializers.IntegerField(allow_null=True, required=False)
    created_at = serializers.DateTimeField(allow_null=True, required=False)
    updated_at = serializers.DateTimeField(allow_null=True, required=False)

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class JobSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), allow_null=True, required=False)
    recruiter = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    title = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    job_description = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    job_type = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    # Add other fields as per your model

    def create(self, validated_data):
        return Job.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class JobApplicationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    # Add other fields as per your model

    def create(self, validated_data):
        return JobApplication.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class ApplicationFeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    application = serializers.PrimaryKeyRelatedField(queryset=JobApplication.objects.all())
    # Add other fields as per your model

    def create(self, validated_data):
        return ApplicationFeedback.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class OfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    application = serializers.PrimaryKeyRelatedField(queryset=JobApplication.objects.all())
    # Add other fields as per your model

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class ActivityLogsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # Add other fields as per your model

    def create(self, validated_data):
        return ActivityLogs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance