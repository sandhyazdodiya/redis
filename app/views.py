from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    User, Candidate, CandidateEducation, Company, Job,
    JobApplication, ApplicationFeedback, Offer, ActivityLogs
)
from .serializers import (
    UserSerializer, CandidateSerializer, CandidateEducationSerializer, CompanySerializer,
    JobSerializer, JobApplicationSerializer, ApplicationFeedbackSerializer, OfferSerializer,
    ActivityLogsSerializer
)

class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            if 'password' in request.data:
                user.set_password(request.data['password'])
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'password' in request.data:
                user.set_password(request.data['password'])
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CandidateAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(Candidate, pk=pk)
            serializer = CandidateSerializer(obj)
            return Response(serializer.data)
        objs = Candidate.objects.all()
        serializer = CandidateSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(Candidate, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Repeat similar for other models:

class CandidateEducationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(CandidateEducation, pk=pk)
            serializer = CandidateEducationSerializer(obj)
            return Response(serializer.data)
        objs = CandidateEducation.objects.all()
        serializer = CandidateEducationSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(CandidateEducation, pk=pk)
        serializer = CandidateEducationSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(CandidateEducation, pk=pk)
        serializer = CandidateEducationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(CandidateEducation, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(Company, pk=pk)
            serializer = CompanySerializer(obj)
            return Response(serializer.data)
        objs = Company.objects.all()
        serializer = CompanySerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(Company, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(Job, pk=pk)
            serializer = JobSerializer(obj)
            return Response(serializer.data)
        objs = Job.objects.all()
        serializer = JobSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(Job, pk=pk)
        serializer = JobSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(Job, pk=pk)
        serializer = JobSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(Job, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobApplicationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(JobApplication, pk=pk)
            serializer = JobApplicationSerializer(obj)
            return Response(serializer.data)
        objs = JobApplication.objects.all()
        serializer = JobApplicationSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(JobApplication, pk=pk)
        serializer = JobApplicationSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(JobApplication, pk=pk)
        serializer = JobApplicationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(JobApplication, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApplicationFeedbackAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(ApplicationFeedback, pk=pk)
            serializer = ApplicationFeedbackSerializer(obj)
            return Response(serializer.data)
        objs = ApplicationFeedback.objects.all()
        serializer = ApplicationFeedbackSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(ApplicationFeedback, pk=pk)
        serializer = ApplicationFeedbackSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(ApplicationFeedback, pk=pk)
        serializer = ApplicationFeedbackSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(ApplicationFeedback, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OfferAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(Offer, pk=pk)
            serializer = OfferSerializer(obj)
            return Response(serializer.data)
        objs = Offer.objects.all()
        serializer = OfferSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(Offer, pk=pk)
        serializer = OfferSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(Offer, pk=pk)
        serializer = OfferSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(Offer, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivityLogsAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(ActivityLogs, pk=pk)
            serializer = ActivityLogsSerializer(obj)
            return Response(serializer.data)
        objs = ActivityLogs.objects.all()
        serializer = ActivityLogsSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivityLogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(ActivityLogs, pk=pk)
        serializer = ActivityLogsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = get_object_or_404(ActivityLogs, pk=pk)
        serializer = ActivityLogsSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(ActivityLogs, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)