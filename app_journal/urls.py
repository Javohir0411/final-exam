from .views import (
    RequirementsViewSet,
    PublicationViewSet,
    InfoAdminViewSet,
    CategoryViewSet,
    ContactViewSet,
    PaperViewSet,
    FAQViewSet,
    main_page,
)
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'paper', PaperViewSet, basename='paper')
router.register(r'publication', PublicationViewSet, basename='publication')
router.register(r'faq', FAQViewSet, basename='faq')
router.register(r'requirements', RequirementsViewSet, basename='requirements')
router.register(r'info-admin', InfoAdminViewSet, basename='info_admin')

urlpatterns = router.urls

urlpatterns += [
    path('main-page/', main_page, name='main_page'),
]
