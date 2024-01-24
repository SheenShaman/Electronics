from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from main.models import Link, Contacts, Product
from main.serializers import LinkSerializer, ContactsSerializer, ProductSerializer


class ContactsViewSet(ModelViewSet):
    """ ViewSet for Contacts """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class ProductViewSet(ModelViewSet):
    """ ViewSet for Products """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class LinkCreateAPIView(generics.CreateAPIView):
    """ Create Link """
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save()


class LinkListAPIView(generics.ListAPIView):
    """ Get Links """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    """ Get Link """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class LinkUpdateAPIView(generics.UpdateAPIView):
    """ Update Link """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def perform_update(self, serializer):
        serializer.save()


class LinkDestroyAPIView(generics.DestroyAPIView):
    """ Delete Link """
    queryset = Link.objects.all()
