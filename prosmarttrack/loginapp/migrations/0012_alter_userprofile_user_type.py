# Generated by Django 4.2.16 on 2024-11-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0011_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('TEACHER', 'Teacher'), ('ADMIN', 'Admin'), ('INSTITUTE', 'Institute')], max_length=20),
        ),
    ]
