# Generated by Django 4.2.17 on 2024-12-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0022_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('INSTITUTE', 'Institute'), ('TEACHER', 'Teacher'), ('ADMIN', 'Admin')], max_length=20),
        ),
    ]
