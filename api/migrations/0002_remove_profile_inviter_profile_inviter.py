# Generated by Django 4.2.4 on 2023-11-11 09:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='inviter',
        ),
        migrations.AddField(
            model_name='profile',
            name='inviter',
            field=models.ManyToManyField(blank=True, null=True, related_name='inviter', to=settings.AUTH_USER_MODEL),
        ),
    ]
