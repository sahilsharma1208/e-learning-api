# Generated by Django 3.2.8 on 2022-04-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_modulename'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainermanagement',
            name='password',
            field=models.CharField(default='hello', max_length=100),
        ),
        migrations.AlterField(
            model_name='traineemanagement',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='traineemanagement',
            name='section',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='trainermanagement',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='trainermanagement',
            name='section',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
