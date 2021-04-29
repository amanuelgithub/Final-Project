from django.db.models.signals import post_save
from django.contrib.auth.models import User
from TrafficReport.models import TrafficPolice
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_traffic_police(sender,instance,created,**kwargs):
    print("created:",created)
    if created:
        TrafficPolice.objects.create(user=instance)


