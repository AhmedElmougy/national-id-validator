import re

from datetime import date, datetime

from rest_framework import serializers

from national_id.governorate_list import GOVERNORATES


class NationalIdValidator:
    """
    validates national id number
    """

    def __call__(self, value):

        # validate general id format
        regex = r"^(?P<century>[23]{1})"\
            "(?P<year>\d{2})"\
            "(?P<month>\d{2})"\
            "(?P<day>\d{2})"\
            "(?P<govcode>\d{2})"\
            "(?P<bseq>\d{3})"\
            "(?P<gender>\d{1})"\
            "(?P<validno>\d{1})"

        # evaluate regexp
        matches = re.search(regex, str(value))
        if matches == None:
            message = 'invalid national id format'
            raise serializers.ValidationError(message)

        # Validate government code digits
        try:
            self.place_of_birth = GOVERNORATES[matches.group('govcode')]
        except:
            message = 'invalid governorate code format'
            raise serializers.ValidationError(message)

        # validate date of birth format
        try:
            self.date_of_birth = date(
                int(matches.group('year')),
                int(matches.group('month')),
                int(matches.group('day'))
            )
        except:
            message = 'invalid birth date format'
            raise serializers.ValidationError(message)

        # validate century digit against birth date
        if matches.group('century') == '3' and \
                (int(matches.group('year'))+2000) > datetime.now().year:
            message = "century and year doesn't match"
            raise serializers.ValidationError(message)
