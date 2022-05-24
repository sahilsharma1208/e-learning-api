from django.shortcuts import render
from rest_framework import generics, mixins
from course.models import InstituteManagement, TrainerManagement, TraineeManagement, ModuleName, ManageBatch, QuestionBank, StatusName, SemesterName, DepartmentName
from course.serializers import InstituteSerializer, TrainerSerializer, TraineeSerializer, ModuleNameSerializer, ManageBatchSerializer, QuestionBankSerializer, StatusNameSerializer, SemesterNameSerializer, DepartmentNameSerializer

# Create your views here.

class InstituteList(generics.ListCreateAPIView):
    queryset = InstituteManagement.objects.all()
    serializer_class = InstituteSerializer


class InstituteDetail(generics.RetrieveUpdateAPIView):
    queryset = InstituteManagement.objects.all()
    serializer_class = InstituteSerializer


class TrainerList(generics.ListCreateAPIView):
    queryset = TrainerManagement.objects.all()
    serializer_class = TrainerSerializer


class TrainerDetail(generics.RetrieveUpdateAPIView):
    queryset = TrainerManagement.objects.all()
    serializer_class = TrainerSerializer


class TraineeList(generics.ListCreateAPIView):
    queryset = TraineeManagement.objects.all()
    serializer_class = TraineeSerializer


class TraineeDetail(generics.RetrieveUpdateAPIView):
    queryset = TraineeManagement.objects.all()
    serializer_class = TraineeSerializer


class ModuleList(generics.ListCreateAPIView):
    queryset = ModuleName.objects.all()
    serializer_class = ModuleNameSerializer


class ModuleDetail(generics.RetrieveUpdateAPIView):
    queryset = ModuleName.objects.all()
    serializer_class = ModuleNameSerializer


class DepartmentNameDetail(generics.RetrieveUpdateAPIView):
    queryset = DepartmentName.objects.all()
    serializer_class = DepartmentNameSerializer


class DepartmentNameList(generics.ListCreateAPIView):
    queryset = DepartmentName.objects.all()
    serializer_class = DepartmentNameSerializer


class BatchList(generics.ListCreateAPIView):
    queryset = ManageBatch.objects.all()
    serializer_class = ManageBatchSerializer


class BatchDetail(generics.RetrieveUpdateAPIView):
    queryset = ManageBatch.objects.all()
    serializer_class = ManageBatchSerializer


class QuestionBankList(generics.ListCreateAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer


class QuestionBankDetail(generics.RetrieveUpdateAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer


class StatusNameDetail(generics.RetrieveUpdateAPIView):
    queryset = StatusName.objects.all()
    serializer_class = StatusNameSerializer


class StatusNameList(generics.ListCreateAPIView):
    queryset = StatusName.objects.all()
    serializer_class = StatusNameSerializer


class SemesterNameDetail(generics.RetrieveUpdateAPIView):
    queryset = SemesterName.objects.all()
    serializer_class = SemesterNameSerializer


class SemesterNameList(generics.ListCreateAPIView):
    queryset = SemesterName.objects.all()
    serializer_class = SemesterNameSerializer


