# Generated by Django 4.2.16 on 2024-12-05 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_remove_studenttable_vehicle_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transpotable',
            name='ROUTE',
        ),
        migrations.RemoveField(
            model_name='transpotable',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='transpotable',
            name='updated_at',
        ),
    ]