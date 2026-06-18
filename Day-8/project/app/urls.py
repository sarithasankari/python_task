from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.StudentView.as_view(),name="student"),
    path('api/<int:id>/',views.StudentView.as_view(),name="student"),


]