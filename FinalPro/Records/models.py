# from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Records(models.Model):
    """Model definition for Records."""
    vehicle_plate=models.IntegerField()
    location=models.PointField()
    address=models.CharField(max_length=50)
    vehicle_speed=models.IntegerField(null=True)
    duration=models.TimeField()
    vehicle_owner=models.CharField(max_length=100)

    created_at=models.DateTimeField(auto_now_add=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Records."""

        verbose_name = 'Records'
        verbose_name_plural = 'Recordss'

    def __str__(self):
        """Unicode representation of Records."""
        return self.address
