# Generated by Django 3.2.8 on 2022-05-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0032_alter_traineemanagement_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traineemanagement',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]