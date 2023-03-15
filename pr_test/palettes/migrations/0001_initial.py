# Generated by Django 4.0.10 on 2023-03-15 12:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
            ],
        ),
    ]
