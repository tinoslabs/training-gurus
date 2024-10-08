# Generated by Django 4.2 on 2024-07-07 09:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_guru_app', '0004_client_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('job_details', ckeditor.fields.RichTextField(max_length=20000)),
                ('posted_date', models.DateField()),
                ('end_date', models.DateField()),
                ('post_end_date', models.DateTimeField()),
            ],
        ),
    ]
