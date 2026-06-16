from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    CUSTUMER = 'client'
    SELLER = 'vendeur'

    ROLE_CHOICES = (
        (CUSTUMER, 'CUSTUMER'),
        (SELLER, 'SELLER'),

    )
    photo_profile = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True) 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTUMER)   