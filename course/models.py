from django.db import models

# Create your models here.

class InstituteManagement(models.Model):
    id = models.AutoField(primary_key=True)
    zone = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    batch = models.CharField(max_length=10)
    trainer = models.CharField(max_length=10)
    trainee = models.CharField(max_length=10)

    class Meta:
        db_table = "institute"

    # def __str__(self):
    #     return self


class TrainerManagement(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    loginName = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    department = models.CharField(blank=True, max_length=100)
    section = models.CharField(blank=True, max_length=100)

    class Meta:
        db_table = "trainer"

    def __str__(self):
        return self


class TraineeManagement(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    loginName = models.CharField(max_length=200)
    department = models.CharField(blank=True, max_length=100)
    section = models.CharField(blank=True, max_length=100)

    class Meta:
        db_table = "trainee"

    # def __str__(self):
    #     return self


class DepartmentName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "department_name"


class ManageBatch(models.Model):
    id = models.AutoField(primary_key=True)
    batchName = models.CharField(max_length=100)
    batchFor = models.CharField(blank=True, max_length=100)
    department = models.ForeignKey(DepartmentName, on_delete=models.CASCADE, related_name="department_id", default=1)
    startDate = models.DateField()
    endDate = models.DateField()
    licenseKey = models.CharField(blank=True, max_length=100)

    class Meta:
        db_table = "manage-batch"



class ModuleName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "module"



class StatusName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'status_name'



class QuestionBank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    numOfQuestions = models.CharField(max_length=100)
    mappingName = models.CharField(max_length=100)
    status = models.ForeignKey(StatusName, on_delete=models.CASCADE, related_name="status_id")

    class Meta:
        db_table = "question_bank"



class SemesterName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "semester_name"