from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from RecordReport.models import Records
from django_extensions.db.models import TimeStampedModel


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
    records=models.OneToOneField(Records,on_delete=models.CASCADE,related_name="report")
    traffic_police=models.OneToOneField(TrafficPolice,on_delete=models.CASCADE)
    status=models.BooleanField("is_reported",default=False)
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
class SystemAdmin(models.Model):
    """Model definition for SystemAdmin."""
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="system_admin")
    phone_number=models.CharField(max_length=50)
    status=models.BooleanField("Active",default=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for SystemAdmin."""

        verbose_name = 'SystemAdmin'
        verbose_name_plural = 'SystemAdmins'

    def __str__(self):
        """Unicode representation of SystemAdmin."""
        return str(self.user.username)
class Notification(models.Model):
    recipient=models.ForeignKey(User,on_delete=models.CASCADE)
    records=models.OneToOneField(Records,on_delete=models.CASCADE)
    content=models.TextField(null=True)


    def __str__(self):
        return str(self.records.vehicle)



class MobileNotification(TimeStampedModel):
    recipient = models.ForeignKey(User, related_name='user_device_notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, default='unread')



class MobileDevices(models.Model):
    participants=models.OneToOneField(User,related_name='device',on_delete=models.CASCADE)
    token=models.TextField()



