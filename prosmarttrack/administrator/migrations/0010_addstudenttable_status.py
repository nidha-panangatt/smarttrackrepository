# Generated by Django 4.2.16 on 2024-12-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_remove_transpotable_route_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudenttable',
            name='status',
            field=models.CharField(blank=True, default='active', max_length=10, null=True),
        ),
    ]