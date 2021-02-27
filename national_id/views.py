from rest_framework import viewsets

from national_id.models import NationalId
from national_id.serializers import NationalIdSerializer


class NationalIdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows National IDs to be viewed, submitted, or edited.
    """
    queryset = NationalId.objects.all()
    serializer_class = NationalIdSerializer
    http_method_names = ['get', 'post', ]
