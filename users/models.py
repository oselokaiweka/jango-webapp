from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *aargs, **kwargs):  # Overrite default model save() for functionality
        super().save(*aargs, **kwargs)  # explicitly running default save method of parent class

        img = Image.open(self.image.path)  # Image associated with current instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            resized_img = ImageOps.fit(img, output_size, Image.ANTIALIAS)
            resized_img.save(self.image.path)
