from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from .models import (
    Category,
    Publication,
    Paper,
    Contact,
    Requirements,
    FAQ, InfoAdmin
)


# PUBLICATION SERIALIZERS
class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"


class PublicationGetSerializer(ModelSerializer):
    publication_name = SerializerMethodField(method_name='get_publication_name', read_only=True)
    publication_description = SerializerMethodField(method_name='get_publication_description', read_only=True)

    class Meta:
        model = Publication
        fields = ('id', 'publication_name', 'journal_avatar', 'publication_description', 'categories_in_journal')

    def get_publication_name(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.journal_name_en
            return obj.journal_name_uz
        except:
            return obj.journal_name_uz

    def get_publication_description(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.journal_description_en
            return obj.journal_description_uz
        except:
            return obj.journal_description_uz


# CATEGORY SERIALIZERS
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryGetSerializer(ModelSerializer):
    category_name = SerializerMethodField(method_name='get_category_name', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'category_name')

    def get_category_name(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.cat_name_en
            return obj.cat_name_uz
        except:
            return obj.cat_name_uz


class PaperSerializer(ModelSerializer):
    class Meta:
        model = Paper
        fields = "__all__"


# PAPER SERIALIZERS
class PaperGetSerializer(ModelSerializer):
    article_name = SerializerMethodField(method_name='get_article_name', read_only=True)
    article_title = SerializerMethodField(method_name='get_article_title', read_only=True)
    article_text = SerializerMethodField(method_name='get_article_text', read_only=True)
    keywords = SerializerMethodField(method_name='get_keywords', read_only=True)

    class Meta:
        model = Paper
        fields = (
            'id', 'created_by', 'article_name', 'article_title', 'article_text', 'references', 'reviewer_file',
            'keywords', 'views_count'
        )
        read_only_fields = ['views_count']

    def get_article_name(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.paper_title_en
            return obj.paper_title_uz
        except:
            return obj.paper_title_uz

    def get_article_title(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.paper_title_en
            return obj.paper_title_uz
        except:
            return obj.paper_title_uz

    def get_article_text(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.paper_text_en
            return obj.paper_text_uz
        except:
            return obj.paper_text_uz

    def get_keywords(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.keywords_en
            return obj.keywords_uz
        except:
            return obj.keywords_uz


# CONTACT SERIALIZERS
class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class InfoAdminSerializer(ModelSerializer):
    class Meta:
        model = InfoAdmin
        fields = "__all__"


class RequirementSerializer(ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"


class RequirementGetSerializer(ModelSerializer):
    req_title = SerializerMethodField(method_name='get_requirements_title', read_only=True)
    req_text = SerializerMethodField(method_name='get_requirements_text', read_only=True)

    class Meta:
        model = Requirements
        fields = ("id", "req_title", "req_text")

    def get_requirements_title(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.requirements_title_en
            return obj.requirements_title_uz
        except:
            return obj.requirements_title_uz

    def get_requirements_text(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.requirements_text_en
            return obj.requirements_text_uz
        except:
            return obj.requirements_text_uz


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class FAQGetSerializer(ModelSerializer):
    fa_questions_question = SerializerMethodField(method_name='get_faq_question', read_only=True)
    fa_questions_answer = SerializerMethodField(method_name='get_faq_answer', read_only=True)

    class Meta:
        model = FAQ
        fields = ("id", "fa_questions_question", "fa_questions_answer")

    def get_fa_questions_question(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.fa_questions_question_en
            return obj.fa_questions_question_uz
        except:
            return obj.fa_questions_question_uz

    def get_fa_questions_answer(self, obj):
        try:
            if self.context['request']['lang'] == 'en':
                return obj.fa_questions_answer_en
            return obj.fa_questions_answer_uz
        except:
            return obj.fa_questions_answer_uz
