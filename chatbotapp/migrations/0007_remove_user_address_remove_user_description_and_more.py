# Generated by Django 4.2.2 on 2024-03-12 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotapp', '0006_book_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='district',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_service',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='website',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
