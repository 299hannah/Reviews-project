# Generated by Django 3.2.5 on 2021-07-20 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210720_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.category'),
        ),
    ]
