# Generated by Django 4.0.4 on 2023-04-17 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_assignment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='status',
        ),
    ]
