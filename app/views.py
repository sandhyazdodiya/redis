from rest_framework import viewsets
from .models import User, Company, Candidate, Job, JobApplication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Candidate
from .serializers import CandidateSerializer

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

class CachedHelloWorld(APIView):
    def get(self, request):
        data = cache.get("hello_world")

        if not data:
            data = {"message": "Hello, World!"}
            cache.set("hello_world", data, timeout=120)  # cache for 60 seconds

        return Response(data)


from rest_framework.views import APIView
from rest_framework.response import Response
from .throttles import RedisRateThrottle

class MyAPIView(APIView):
    throttle_classes = [RedisRateThrottle]

    def get(self, request):
        return Response({"msg": "You are within the limit!"})


class CandidateListCreateAPIView(APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetailAPIView(APIView):
    def get(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        candidate.delete()
        return Response({"message": "Candidate deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



