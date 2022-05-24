from rest_framework import serializers
from course.models import InstituteManagement, TrainerManagement, TraineeManagement, ModuleName, ManageBatch, QuestionBank, StatusName, SemesterName, DepartmentName


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteManagement
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerManagement
        fields = "__all__"


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraineeManagement
        fields = "__all__"


class ModuleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleName
        fields = "__all__"


class DepartmentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentName
        fields = "__all__"


class ManageBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageBatch
        fields = "__all__"


class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = "__all__"


class StatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusName
        fields = "__all__"


class SemesterNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterName
        fields = "__all__"