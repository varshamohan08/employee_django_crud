from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True, verbose_name='User Photo', help_text='Max 5 MB file size')

    def __str__(self):
        return self.name
