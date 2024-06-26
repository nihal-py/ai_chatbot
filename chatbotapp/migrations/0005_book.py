# Generated by Django 4.2.2 on 2024-02-18 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotapp', '0004_alter_user_is_service_alter_user_is_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_date', models.DateField()),
                ('confirm_date', models.DateField(blank=True, null=True)),
                ('user_booking_status', models.CharField(default='Pending', max_length=20)),
                ('service_center_booking_status', models.CharField(default='Pending', max_length=20)),
                ('service_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_center_books', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
