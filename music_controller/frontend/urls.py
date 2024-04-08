from .views import index
from django.urls import path


urlpatterns = [
    path("",index),
    path("create",index),
    path("join",index),
    path("room/<str:roomCode>",index)
]