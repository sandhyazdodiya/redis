from rest_framework import viewsets
from .models import User, Company, Candidate, Job, JobApplication
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


