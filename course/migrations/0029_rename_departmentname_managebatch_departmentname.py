# Generated by Django 3.2.8 on 2022-05-23 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0028_rename_department_managebatch_departmentname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managebatch',
            old_name='departmentName',
            new_name='DepartmentName',
        ),
    ]
