# Generated by Django 4.2.16 on 2024-11-20 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_rename_transpotation_studenttable_transportation_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guardiantable',
            old_name='studentid',
            new_name='admissionno',
        ),
        migrations.RemoveField(
            model_name='guardiantable',
            name='studentname',
        ),
    ]
