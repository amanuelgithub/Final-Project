from django.db.models.signals import post_save
from django.contrib.auth.models import User
from TrafficReport.models import TrafficPolice,SystemAdmin
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("created: ",created)
    if created:
        if instance.is_staff !=True:
            TrafficPolice.objects.create(user=instance)

        else:
            SystemAdmin.objects.create(user=instance)

 
