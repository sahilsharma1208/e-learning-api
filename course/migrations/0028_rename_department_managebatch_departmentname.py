# Generated by Django 3.2.8 on 2022-05-23 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0027_alter_questionbank_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managebatch',
            old_name='department',
            new_name='departmentName',
        ),
    ]
