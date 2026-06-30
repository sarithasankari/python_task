from django.urls import path
from . import views

urlpatterns = [
    path("",views.StudentView.as_view(),name="Student"),
    path('<int:id>',views.StudentView.as_view(),name="Student"),
    
]