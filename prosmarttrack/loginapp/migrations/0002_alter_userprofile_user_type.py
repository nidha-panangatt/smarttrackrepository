# Generated by Django 4.2.16 on 2024-11-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('TEACHER', 'Teacher'), ('ADMIN', 'Admin'), ('INSTITUTE', 'Institute')], max_length=20),
        ),
    ]
