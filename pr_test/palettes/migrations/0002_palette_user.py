# Generated by Django 4.0.10 on 2023-03-15 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('palettes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='palette',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='palettes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]