# Generated by Django 5.0.4 on 2024-05-19 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_journal', '0006_alter_paper_references'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_name',
            new_name='cat_name_uz',
        ),
    ]