# Generated by Django 5.1.6 on 2025-04-14 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albedo', '0003_auto_20250414_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={'verbose_name': 'Решение', 'verbose_name_plural': 'Решения'},
        ),
        migrations.AddField(
            model_name='file',
            name='preview_url',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='URL предпросмотра'),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='albedo.file', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='event',
            name='limit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Срок сдачи'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('in_progress', 'В процессе'), ('closed', 'Закрыто')], default='in_progress', max_length=11, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='file',
            name='cloudinary_url',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Cloudinary URL'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(max_length=255, verbose_name='Имя файла'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.CharField(max_length=255, verbose_name='Путь к файлу'),
        ),
        migrations.AlterField(
            model_name='file',
            name='mime_type',
            field=models.CharField(max_length=50, verbose_name='MIME тип'),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.PositiveIntegerField(verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='albedo.event', verbose_name='Событие'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solutions', to='albedo.file', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
