# Generated by Django 3.2.8 on 2022-05-04 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_questionbank_statusname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.statusname'),
        ),
    ]
