# Generated by Django 4.2.16 on 2024-11-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_alter_userprofile_status_alter_userprofile_user_type'),
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
            field=models.CharField(choices=[('INSTITUTE', 'Institute'), ('ADMIN', 'Admin'), ('TEACHER', 'Teacher')], max_length=20),
        ),
    ]