# Generated by Django 4.2 on 2024-07-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_guru_app', '0012_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career_model',
            name='post_end_date',
        ),
        migrations.AlterField(
            model_name='career_model',
            name='end_date',
            field=models.DateTimeField(),
        ),
    ]
