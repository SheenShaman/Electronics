from django.urls import path

from main.apps import MainConfig
from main.views import LinkCreateAPIView, LinkListAPIView, LinkRetrieveAPIView, LinkUpdateAPIView, LinkDestroyAPIView

app_name = MainConfig.name

urlpatterns = [
    path('link/create/', LinkCreateAPIView.as_view(), name='link_create'),
    path('links/', LinkListAPIView.as_view(), name='link_list'),
    path('link/<int:pk>/', LinkRetrieveAPIView.as_view(), name='link_get'),
    path('link/update/<int:pk>/', LinkUpdateAPIView.as_view(), name='link_update'),
    path('link/delete/<int:pk>/', LinkDestroyAPIView.as_view(), name='link_delete'),
]
