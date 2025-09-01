from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CachedHelloWorld, MyAPIView, CandidateListCreateAPIView, CandidateDetailAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('cache/', CachedHelloWorld.as_view()),
    path('ratelimiting/', MyAPIView.as_view()),
    path("candidates/", CandidateListCreateAPIView.as_view(), name="candidate-list-create"),
    path("candidates/<int:pk>/", CandidateDetailAPIView.as_view(), name="candidate-detail"),

]


# create
# curl --location 'http://127.0.0.1:8000/candidates/' \
# --header 'Content-Type: application/json' \
# --data '{
#     "dob": "2025-09-09",
#     "gender": "Male",
#     "address": "75, Gayatri Society",
#     "resume_url": "http://127.0.0.1:8000/admin/app/candidate/add/",
#     "experience": 6,
#     "skills": {
#         "1": "Python",
#         "2": "Django"
#     },
#     "education": "B.tech",
#     "candidate": 1
# }'


# get one
# curl --location 'http://127.0.0.1:8000/candidates/3' \
# --data ''

# get all
# curl --location 'http://127.0.0.1:8000/candidates/' \
# --data ''

# delete
# curl --location --request DELETE 'http://127.0.0.1:8000/candidates/1/' \
# --data ''


# update
# curl --location --request PATCH 'http://127.0.0.1:8000/candidates/3/' \
# --header 'Content-Type: application/json' \
# --data ' {
#         "id": 3,
#         "dob": "2025-09-09",
#         "gender": "Female",
#         "address": "75, Gayatri Society",
#         "resume_url": "http://127.0.0.1:8000/admin/app/candidate/add/",
#         "experience": 6,
#         "skills": {
#             "1": "Python",
#             "2": "Django"
#         },
#         "education": "B.E",
#         "candidate": 1
#     }'


#put

# curl --location --request PUT 'http://127.0.0.1:8000/candidates/3/' \
# --header 'Content-Type: application/json' \
# --data ' {
#         "id": 3,
#         "dob": "2025-09-09",
#         "gender": "Male",
#         "address": "75, Gayatri Society",
#         "resume_url": "http://127.0.0.1:8000/admin/app/candidate/add/",
#         "experience": 6,
#         "skills": {
#             "1": "Python",
#             "2": "Django"
#         },
#         "education": "B.E",
#         "candidate": 1
#     }'