# Generated by Django 3.2.8 on 2022-05-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_alter_departmentname_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentname',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
