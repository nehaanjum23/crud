from django.urls import path
from .views import StudentView,StudentGetView,StudentUpdateView,StudentDeleteView
urlpatterns = [
   path('create-student/', StudentView.as_view(), name='create-student'),
   path('student-get/', StudentGetView.as_view(), name='Get-student'),
   path('student-update/<int:id>/', StudentUpdateView.as_view(), name='Update-student'),
   path('student-delete/int:id>/', StudentDeleteView.as_view(), name='Delete-student'),
]