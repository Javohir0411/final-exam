# Generated by Django 5.0.4 on 2024-05-19 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_journal', '0008_rename_journal_description_publication_journal_description_uz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='faq_answer',
            new_name='faq_answer_uz',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='faq_question',
            new_name='faq_question_uz',
        ),
    ]