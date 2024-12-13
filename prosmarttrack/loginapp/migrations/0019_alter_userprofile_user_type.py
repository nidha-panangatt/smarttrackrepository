# Generated by Django 4.2.17 on 2024-12-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0018_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('INSTITUTE', 'Institute'), ('TEACHER', 'Teacher')], max_length=20),
        ),
    ]
