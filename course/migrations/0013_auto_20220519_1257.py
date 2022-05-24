# Generated by Django 3.2.8 on 2022-05-19 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20220519_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentname',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='departmentname',
            name='name',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='managebatch',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.departmentname'),
        ),
        migrations.AlterField(
            model_name='managebatch',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='semestername',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statusname',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
