# Generated by Django 3.2.5 on 2021-07-20 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_projects_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
    ]
