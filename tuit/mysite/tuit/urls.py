from . import views
from django.urls import path


urlpatterns = [
    path('faculty/', views.FacultyView.as_view()),
    path('faculty/<int:pk>/', views.FacultyView.as_view()),

    path('group/', views.GroupView.as_view()),
    path('group/<int:pk>/', views.GroupView.as_view()),

    path('subject/', views.SubjectVeiw.as_view()),
    path('subject/<int:pk>/', views.SubjectVeiw.as_view()),

    path('student/', views.StudentVeiw.as_view()),
    path('student/<int:pk>/', views.StudentVeiw.as_view()),

    path('teacher/', views.TeacherVeiw.as_view()),
    path('teacher/<int:pk>/', views.TeacherVeiw.as_view()),
]