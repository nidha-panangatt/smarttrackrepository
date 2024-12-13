# Generated by Django 4.2.17 on 2024-12-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0015_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('INSTITUTE', 'Institute'), ('TEACHER', 'Teacher'), ('ADMIN', 'Admin')], max_length=20),
        ),
    ]
