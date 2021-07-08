from django.db.models.signals import post_save
from django.contrib.auth.models import User
from TrafficReport.models import Notification, TrafficPolice,SystemAdmin,MobileNotification
from RecordReport.models import Records
from django.dispatch import receiver
from django.conf import settings
from pyfcm import FCMNotification


@receiver(post_save,sender=User)
def register_user(sender, instance, created, **kwargs):
    print("created: ",created)
    if created:
        if instance.is_staff !=True:
            TrafficPolice.objects.create(user=instance)

        else:
            SystemAdmin.objects.create(user=instance)






@receiver(post_save,sender=Records)
def notifie_user(sender,instance,created,**kwargs):
    print('created: ',created)
    user_id=User.objects.filter(pk=1)
    if created:
        Notification.objects.create(records=instance,recipient=user_id.first())



#  Notification Triggering 

@receiver(post_save, sender=Notification)
def send_new_message_notification(sender, **kwargs):
    message = kwargs['instance']
    send_new_message_push_notification(sender_id=message.records.id,
                                       recipient_id=message.recipient.id,
                                       content=message.content)



def send_new_message_push_notification(**kwargs):
    sender=Records.objects.get(id=kwargs.get('sender_id'))
    recipient=User.objects.get(id=kwargs.get('recipient_id'))
    content = kwargs.get("content")
    notification=MobileNotification()
    notification.recipient = recipient
    notification.title = "New notification"
    # sender_full_name = "{} {}".format(sender.first_name, 
    #                                   sender.last_name)
    message = '{} has sent you a message: "{}"'.format(content)
    notification.message = message
    data_payload = {
            "badge": recipient.unread_notifications_count(),
            "alert": notification.title,
            "notification_id": notification.pk,
            "body": notification.message,
        }



    fcm = FCMNotification(api_key=settings.FIREBASE_API_KEY)
    return fcm.notify_single_device(
            registration_id=str(recipient.device.token),
            badge=recipient.unread_notifications_count(),
            data_message=data_payload,
            message_body=content)





    
