from django.urls import path
from . import views
urlpatterns = [
    path('Generics/',views.StudentView.as_view()),  
    path('GenericsCreate/',views.StudentCreate.as_view()),  
    path('GenericsRetrive/<int:pk>/',views.StudentUpdate.as_view()),
    path('GenericsUpdate/<int:pk>/',views.StudentUpdate.as_view()),
    path('GenericsDelete/<int:pk>/',views.StudentUpdate.as_view()),  
]