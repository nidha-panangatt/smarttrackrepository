# Generated by Django 4.2.16 on 2024-11-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_rename_studentid_guardiantable_admissionno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttable',
            name='student_image',
            field=models.FileField(blank=True, null=True, upload_to='student_image'),
        ),
    ]
