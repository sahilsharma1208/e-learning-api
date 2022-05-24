from django.urls import path
from course import views

urlpatterns = [
    path('institute-managements/', views.InstituteList.as_view()),
    path('institute-management/<int:pk>', views.InstituteDetail.as_view()),
    path('trainer-managements/', views.TrainerList.as_view()),
    path('trainer-management/<int:pk>', views.TrainerDetail.as_view()),
    path('trainee-managements/', views.TraineeList.as_view()),
    path('trainee-management/<int:pk>', views.TraineeDetail.as_view()),
    path('module-name/<int:pk>', views.ModuleDetail.as_view()),
    path('module-names/', views.ModuleList.as_view()),
    path('manage-batch/<int:pk>', views.BatchDetail.as_view()),
    path('manage-batches/', views.BatchList.as_view()),
    path('status-names/', views.StatusNameList.as_view()),
    path('status-name/<int:pk>', views.StatusNameDetail.as_view()),
    path('question-bank/<int:pk>', views.QuestionBankDetail.as_view()),
    path('question-banks/', views.QuestionBankList.as_view()),
    path('semester/<int:pk>', views.SemesterNameDetail.as_view()),
    path('semesters/', views.SemesterNameList.as_view()),
    path('department/<int:pk>', views.DepartmentNameDetail.as_view()),
    path('departments/', views.DepartmentNameList.as_view()),
]