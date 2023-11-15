# Generated by Django 4.2.4 on 2023-11-11 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_remove_profile_inviter_profile_inviter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='inviter',
        ),
        migrations.AddField(
            model_name='profile',
            name='inviter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL),
        ),
    ]
