# Generated by Django 3.2.8 on 2022-05-23 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0029_rename_departmentname_managebatch_departmentname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managebatch',
            name='DepartmentName',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='department_id', to='course.departmentname'),
        ),
    ]
