from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,unique=True,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profiles/',blank=True,null=True)

    def __str__(self):
        return self.username
