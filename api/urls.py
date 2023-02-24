from home.views import PersonAPI, RegisterAPI, LoginAPI
from django.urls import path

urlpatterns = [
    # path('person/', person),
    path('register/',RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    # path('login/', login),
    path('persons/',PersonAPI.as_view()),
]
