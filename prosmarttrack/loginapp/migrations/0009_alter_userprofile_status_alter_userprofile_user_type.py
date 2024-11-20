# Generated by Django 4.2.16 on 2024-11-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0008_alter_userprofile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('TEACHER', 'Teacher'), ('INSTITUTE', 'Institute')], max_length=20),
        ),
    ]
