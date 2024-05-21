# Generated by Django 5.0.4 on 2024-05-17 18:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cat_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('faq_question', models.CharField(max_length=300)),
                ('faq_answer', models.TextField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
                'db_table': 'faq',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paper_name', models.CharField(max_length=200)),
                ('paper_title', models.CharField(max_length=355)),
                ('paper_text', models.TextField()),
                ('references', ckeditor.fields.RichTextField()),
                ('reviewer_file', models.FileField(upload_to='reviewer-file/')),
                ('keywords', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Papers',
                'db_table': 'papers',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('journal_name', models.CharField(max_length=155)),
                ('journal_description', models.CharField(max_length=355)),
                ('journal_file', models.FileField(upload_to='journal-files/')),
                ('journal_avatar', models.ImageField(upload_to='journal-images/')),
            ],
            options={
                'verbose_name_plural': 'Publications',
                'db_table': 'publications',
            },
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requirement_title', models.CharField(max_length=355)),
                ('requirement_text', models.TextField()),
            ],
            options={
                'verbose_name': 'Requirement',
                'verbose_name_plural': 'Requirements',
            },
        ),
    ]