# Generated by Django 3.2.8 on 2022-05-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0031_auto_20220523_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traineemanagement',
            name='department',
            field=models.CharField(max_length=100),
        ),
    ]
