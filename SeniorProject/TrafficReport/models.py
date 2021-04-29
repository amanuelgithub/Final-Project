from django.db import models
from django.contrib.auth.models import User
from RecordReport.models import Records

# Create your models here.




class TrafficPolice(models.Model):
    """Model definition for TrafficPolice."""
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=100)
    status=models.BooleanField("Active",default=True, )

    # TODO: Define fields here

    class Meta:
        """Meta definition for TrafficPolice."""

        verbose_name = 'TrafficPolice'
        verbose_name_plural = 'TrafficPolices'

    def __str__(self):
        """Unicode representation of TrafficPolice."""
        return self.user.username


class Report(models.Model):
    """Model definition for Report."""
    description=models.TextField()
    records=models.OneToOneField(Records,on_delete=models.CASCADE)
    traffic_police=models.OneToOneField(TrafficPolice,on_delete=models.CASCADE)
    status=models.BooleanField("is_approved",default=False)
    created_at=models.DateTimeField(auto_now_add=True)



    # TODO: Define fields here

    class Meta:
        """Meta definition for Report."""

        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

        permissions=(
            ('read_repor','can read report'),
        )

    def __str__(self):
        """Unicode representation of Report."""
        pass
