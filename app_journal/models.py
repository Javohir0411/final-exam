from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = "abstract_model"


class Category(AbstractBaseModel):
    cat_name_uz = models.CharField(max_length=100)
    cat_name_en = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cat_name_uz} | {self.cat_name_en}"

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class Paper(AbstractBaseModel):
    paper_name_uz = models.CharField(max_length=200)
    paper_name_en = models.CharField(max_length=200)
    paper_title_uz = models.CharField(max_length=355)
    paper_title_en = models.CharField(max_length=355)
    paper_text_uz = models.TextField()
    paper_text_en = models.TextField()
    references = RichTextField(null=True, blank=True)
    reviewer_file = models.FileField(upload_to='reviewer-file/')
    keywords_uz = models.CharField(max_length=100)
    keywords_en = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.paper_name_uz} | {self.paper_title_uz}"

    class Meta:
        verbose_name_plural = 'Papers'
        db_table = 'papers'


class Publication(AbstractBaseModel):
    journal_name_uz = models.CharField(max_length=155)
    journal_name_en = models.CharField(max_length=155)
    journal_description_uz = models.CharField(max_length=355)
    journal_description_en = models.CharField(max_length=355)
    categories_in_journal = models.ForeignKey(Category, on_delete=models.CASCADE)
    journal_file = models.FileField(upload_to='journal-files/')
    journal_avatar = models.ImageField(upload_to='journal-images/')
    paper = models.ForeignKey(Paper, related_name='publications', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.journal_name_uz} | {self.journal_description_uz}"

    class Meta:
        verbose_name_plural = 'Publications'
        db_table = 'publications'


class Requirements(AbstractBaseModel):
    requirement_title = models.CharField(max_length=355)
    requirement_title_en = models.CharField(max_length=355)
    requirement_text = models.TextField()
    requirement_text_en = models.TextField()

    def __str__(self):
        return f"{self.requirement_title} | {self.requirement_text}"

    class Meta:
        verbose_name_plural = 'Requirements'
        verbose_name = 'Requirement'


class FAQ(AbstractBaseModel):
    faq_question_uz = models.CharField(max_length=300)
    faq_question_en = models.CharField(max_length=300)
    faq_answer_uz = models.TextField()
    faq_answer_en = models.TextField()

    def __str__(self):
        return f"{self.faq_question_uz} | {self.faq_answer_uz}"

    class Meta:
        verbose_name_plural = 'FAQ'
        verbose_name = 'FAQ'
        db_table = 'faq'


class Contact(AbstractBaseModel):
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.firstname} | {self.message}"

    class Meta:
        verbose_name_plural = 'Contact'
        verbose_name = 'Contact'
        db_table = 'contact'


class InfoAdmin(AbstractBaseModel):
    admin_address = models.CharField(max_length=400)
    admin_phone_number = models.CharField(max_length=20)
    admin_email = models.EmailField()

    def __str__(self):
        return f"{self.admin_address} | {self.admin_phone_number} | {self.admin_email}"

    class Meta:
        verbose_name_plural = "InfoAdmins"
        verbose_name = "InfoAdmin"
        db_table = 'info-admins'

