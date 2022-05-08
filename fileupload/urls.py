from django.urls import path
from .views import Home, upload


urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('upload/', upload, name='upload'),
]
