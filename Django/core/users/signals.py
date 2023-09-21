from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.signals import user_logged_in


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile created ",instance)
    else:       
        instance.profile.save()
        print("profile updated ",instance)



# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):

@receiver(user_logged_in, sender=User)
def logged_in(sender, request, user, **kwargs):
    print("-------logged in-----------")
    print(sender)
    print(request)
    print(user)
    print("------------------------")

