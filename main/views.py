from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import Link
from main.serializers import LinkSerializer


class LinkCreateAPIView(generics.CreateAPIView):
    """ Create Link """
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]


class LinkListAPIView(generics.ListAPIView):
    """ Get Links """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    """ Get Link """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkUpdateAPIView(generics.UpdateAPIView):
    """ Update Link """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkDestroyAPIView(generics.DestroyAPIView):
    """ Delete Link """
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]
