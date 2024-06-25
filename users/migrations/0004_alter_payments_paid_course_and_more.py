# Generated by Django 5.0.6 on 2024-06-25 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_course_preview_alter_lesson_preview'),
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='Оплаченный урок'),
        ),
    ]