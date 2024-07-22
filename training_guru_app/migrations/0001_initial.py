# Generated by Django 4.2 on 2024-07-07 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_image', models.ImageField(blank=True, null=True, upload_to='client_images/')),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('review', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
