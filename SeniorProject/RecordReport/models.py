from django.db import models

# Create your models here.
from django.contrib.gis.db import models

# Create your models here.


class Vehicle(models.Model):
    """Model definition for Vehicle."""
    vehicle_plate=models.IntegerField()
    vehicle_type=models.CharField(max_length=100)
    vehicle_owner=models.CharField(max_length=100)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Vehicle."""

        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        """Unicode representation of Vehicle."""
        return str(self.vehicle_plate)

class Records(models.Model):
    """Model definition for Records."""
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="records")
    location=models.PointField()
    address=models.CharField(max_length=50)
    vehicle_speed=models.IntegerField(null=True)
    duration=models.TimeField()

    created_at=models.DateTimeField(auto_now_add=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Records."""

        verbose_name = 'Records'
        verbose_name_plural = 'Records'

    def __str__(self):
        """Unicode representation of Records."""
        return self.address
