# Generated by Django 5.0.3 on 2024-05-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='login',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
