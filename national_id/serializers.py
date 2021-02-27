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

    def create(self, validated_data):
        """
        extract info from national id number and save
        these values upon creation
        """
        national_id = validated_data['national_id']
        nid = str(national_id)
        year = int(nid[1:3])
        if int(nid[0]) == 2:
            year += 1900  # 2 -> add 20th century (1900)
        else:
            year += 2000  # 3 -> add 21th century (2000)

        validated_data['date_of_birth'] = date(
            year, int(nid[3:5]), int(nid[5:7]))

        validated_data['place_of_birth'] = GOVERNORATES[nid[7:9]]

        # digit 13 represents gender even -> femal, odd -> male
        if int(int(nid[12])) % 2 == 0:
            validated_data['gender'] = 'Female'
        else:
            validated_data['gender'] = 'Male'

        return NationalId.objects.create(**validated_data)
