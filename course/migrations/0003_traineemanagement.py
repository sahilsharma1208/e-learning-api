# Generated by Django 3.2.8 on 2022-04-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_trainermanagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraineeManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('loginName', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'trainee',
            },
        ),
    ]
