from django_filters import rest_framework as filters

from app_journal.models import Paper, Publication


class PaperFilter(filters.FilterSet):
    paper_name_uz = filters.CharFilter(lookup_expr='icontains')
    paper_name_en = filters.CharFilter(lookup_expr='icontains')
    paper_title_uz = filters.CharFilter(lookup_expr='icontains')
    paper_title_en = filters.CharFilter(lookup_expr='icontains')
    keywords_uz = filters.CharFilter(lookup_expr='icontains')
    keywords_en = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Paper
        fields = ['paper_name_uz', 'paper_name_en', 'paper_title_uz', 'paper_title_en', 'keywords_uz', 'keywords_en']


class PublicationFilter(filters.FilterSet):
    journal_name_uz = filters.CharFilter(lookup_expr='icontains')
    journal_name_en = filters.CharFilter(lookup_expr='icontains')
    journal_description_uz = filters.CharFilter(lookup_expr='icontains')
    journal_description_en = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Publication
        fields = ['journal_name_uz', 'journal_name_en' 'journal_description_uz', 'journal_description_en']
