from django.db import models


class NationalId(models.Model):
    """
    Egyption National Id model representation
    """

    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    national_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=16, default='')
    gender = models.CharField(max_length=1, choices=GENDER, default='')

    def __str__(self):

        return str(self.national_id)
