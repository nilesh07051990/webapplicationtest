# Generated by Django 5.1 on 2024-10-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_alter_employee_eno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eaddr',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='employee',
            name='esal',
            field=models.IntegerField(),
        ),
    ]