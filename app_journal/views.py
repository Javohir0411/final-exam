from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (
    Requirements,
    Publication,
    InfoAdmin,
    Category,
    Contact,
    Paper,
    FAQ,
)
from .permissions import IsOwnerOrAuthenticated
from .serializers import (
    PublicationGetSerializer,
    RequirementGetSerializer,
    PublicationSerializer,
    RequirementSerializer,
    CategoryGetSerializer,
    InfoAdminSerializer,
    PaperGetSerializer,
    CategorySerializer,
    ContactSerializer,
    PaperSerializer,
    FAQSerializer,
)


# Main sahifasida LAST EDITION, LAST PAPER va MOST READ PAPERS Ma'lumotlarini qaytarish uchun view
@api_view(["GET"])
def main_page(request):
    paper_serializer = PaperSerializer(Paper.objects.all().last())
    latest_paper_serializer = PaperGetSerializer(
        Paper.objects.all().order_by('created_at')[:10],
        many=True
    )
    top_paper_serializer = PaperGetSerializer(
        Paper.objects.all().order_by('views_count')[:10],
        many=True
    )
    return Response(
        data={
            "PAPER": paper_serializer.data,
            "latest_PAPER": latest_paper_serializer.data,
            "top_paper": top_paper_serializer.data,
        }
    )


# class PaperDetailView(RetrieveAPIView):
#     queryset = Paper.objects.all()
#     serializer_class = PaperSerializer
#     lookup_field = 'id'


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrAuthenticated,
                          IsAuthenticated]  # 'permission_classes' ro'yxat sifatida iterable bo'lishi kerak


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsOwnerOrAuthenticated,
                          IsAuthenticated]  # 'permission_classes' ro'yxat sifatida iterable bo'lishi kerak

    def get_serializer_class(self):
        if self.request.method == "GET":  # GET method bo'lganda "CategoryGetSerializer qaytaradi"
            return CategoryGetSerializer
        return CategorySerializer  # Aks holda (method POST bo'lganda ) "CategorySerializer qaytaradi"


class PaperViewSet(ModelViewSet):
    queryset = Paper.objects.all()
    permission_classes = [IsOwnerOrAuthenticated,
                          IsAuthenticated]  # 'permission_classes' ro'yxat sifatida iterable bo'lishi kerak

    def get_serializer_class(self):
        if self.request.method == "GET":  # GET method bo'lganda "PaperGetSerializerni qaytaradi"
            return PaperGetSerializer
        return PaperSerializer  # Aks holda (method POST bo'lganda ) "PaperSerializerni qaytaradi"

    def retrieve(self, request, *args, **kwargs):
        instance = Paper.objects.get(pk=self.kwargs["pk"])
        instance.views_count += 1
        instance.save()

        return super().retrieve(request, *args, **kwargs)


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    permission_classes = [IsOwnerOrAuthenticated,
                          IsAuthenticated]  # 'permission_classes' ro'yxat sifatida iterable bo'lishi kerak

    def get_serializer_class(self):
        if self.request.method == "GET":  # GET method bo'lganda "PublicationGetSerializerni qaytaradi"
            return PublicationGetSerializer
        return PublicationSerializer  # Aks holda (method POST bo'lganda ) "PublicationSerializerni qaytaradi"


class RequirementsViewSet(ModelViewSet):
    queryset = Requirements.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":  # GET method bo'lganda "RequirementGetSerializer qaytaradi"
            return RequirementGetSerializer
        return RequirementSerializer  # Aks holda (method POST bo'lganda ) "RequirementSerializer qaytaradi"


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsOwnerOrAuthenticated,
                          IsAuthenticated]  # 'permission_classes' ro'yxat sifatida iterable bo'lishi kerak


class InfoAdminViewSet(ModelViewSet):
    queryset = InfoAdmin.objects.all()
    serializer_class = InfoAdminSerializer
    permission_classes = [IsOwnerOrAuthenticated,
                          IsAuthenticated]  # 'permission_classes' ro'yxat sifatida iterable bo'lishi kerak
