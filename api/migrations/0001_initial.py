# Generated by Django 4.2.4 on 2023-08-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CN', 'Название сайта'), ('AN', 'Объявление')], default='AN', max_length=2)),
                ('text', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]
