from django.db import models
from django.contrib.auth.models import User , AbstractUser
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

# class CustomUser(AbstractUser):
#     is_adult = models.BooleanField()


