from datetime import date

from django.core.validators import MaxValueValidator

from rest_framework import serializers

from national_id.models import NationalId
from national_id.validators import NationalIdValidator
from national_id.governorate_list import GOVERNORATES


class NationalIdSerializer(serializers.ModelSerializer):
    """ 
    National ID model serializer 
    """

    national_id = serializers.IntegerField(
        validators=[
            NationalIdValidator(),
            MaxValueValidator(99999999999999),
        ]
    )

    class Meta:

        model = NationalId
        fields = ('id', 'national_id', 'date_of_birth',
                  'place_of_birth', 'gender')
        read_only_fields = ('date_of_birth', 'place_of_birth', 'gender')
