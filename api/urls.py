from django.urls import path
from . import views
urlpatterns = [
    path('stu/',views.studentView.as_view()),
    path('stuget/',views.studentGetView.as_view()),
    path('stupdate/<int:id>/',views.studentUpdateView.as_view()),
    path('studel/<int:id>/',views.studentDeleteView.as_view()),
    path('semail/',views.studentemailView.as_view()),
    path('sgetemail/',views.studentemailGetView.as_view()),
    path('supdateemail/<int:id>/',views.studentemailUpdateView.as_view()),
    path('studelemail/<int:id>/',views.studentemailDeleteView.as_view()), 
]