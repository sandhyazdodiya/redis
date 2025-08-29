from rest_framework import serializers
from .models import User, Company, Candidate, Job, JobApplication

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()