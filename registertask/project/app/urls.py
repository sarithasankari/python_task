from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentView,name='request'),
    path('list',views.StudentView,name='list'),
]
