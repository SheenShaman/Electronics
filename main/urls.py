from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import (LinkCreateAPIView, LinkListAPIView, LinkRetrieveAPIView, LinkUpdateAPIView, LinkDestroyAPIView,
                        ContactsViewSet, ProductViewSet)

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contacts')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('link/create/', LinkCreateAPIView.as_view(), name='link_create'),
    path('links/', LinkListAPIView.as_view(), name='link_list'),
    path('link/<int:pk>/', LinkRetrieveAPIView.as_view(), name='link_get'),
    path('link/update/<int:pk>/', LinkUpdateAPIView.as_view(), name='link_update'),
    path('link/delete/<int:pk>/', LinkDestroyAPIView.as_view(), name='link_delete'),
] + router.urls
