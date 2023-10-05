# Generated by Django 3.2.6 on 2023-09-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_profile_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='type',
            field=models.CharField(choices=[('SC', 'Основной цвет сайта'), ('RN', 'Название комнаты'), ('AB', 'Блок с объявлением'), ('EMC', 'Цветная полоса рано утром'), ('MC', 'Цветная полоса утром'), ('DAC', 'Цветная полоса днем'), ('EC', 'Цветная полоса вечером'), ('SO', 'Активный вариант ответа'), ('VB', 'Кнопка отправки голоса'), ('violet', 'Фиолетовый'), ('d_blue', 'Темно-синий'), ('yellow', 'Желтый'), ('pink', 'Розовый'), ('red', 'Красный'), ('blue', 'Синий'), ('green', 'Зеленый'), ('gray', 'Серый'), ('cherry', 'Вишневый'), ('orange', 'Оранжевый')], default='RN', max_length=6),
        ),
    ]
