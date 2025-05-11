from django.urls import path
from app.views import homework5

urlpatterns = [
    path(
        "homework-querysets/", homework5.homework_querysets, name="homework_querysets"
    ),
]
