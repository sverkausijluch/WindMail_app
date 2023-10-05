# Generated by Django 3.2.6 on 2023-09-07 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_room_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='color',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color', to='api.color'),
        ),
    ]
