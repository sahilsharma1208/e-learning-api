# Generated by Django 3.2.8 on 2022-05-19 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_alter_managebatch_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managebatch',
            name='department',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.departmentname'),
        ),
    ]
