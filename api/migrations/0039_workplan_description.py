# Generated by Django 3.2.6 on 2023-09-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_workplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='workplan',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
