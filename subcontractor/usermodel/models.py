from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields
    company_name = models.CharField(max_length=255)
    proprietor_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()

    # User modes
    USER_MODES = (
        ('poster', 'Poster'),
        ('bidder', 'Bidder'),
    )
    mode = models.CharField(max_length=10, choices=USER_MODES)

    def is_poster(self):
        return self.mode == 'poster'

    def is_bidder(self):
        return self.mode == 'bidder'
