from django.urls import path
# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]