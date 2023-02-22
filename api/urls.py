from home.views import person, login
from django.urls import path

urlpatterns = [
    path('person/',person),
    path('login/',login),
]
