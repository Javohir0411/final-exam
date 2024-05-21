# Generated by Django 5.0.4 on 2024-05-19 16:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_journal', '0009_rename_faq_answer_faq_faq_answer_uz_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_address', models.CharField(max_length=400)),
                ('admin_phone_number', models.CharField(max_length=20)),
                ('admin_email', models.EmailField(max_length=254)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'InfoAdmin',
                'verbose_name_plural': 'InfoAdmins',
                'db_table': 'info-admins',
            },
        ),
    ]
