from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass 

    # this class is used for adding things to the user profile
    # (besides username and email)
    # such as profile image

    def __str__(self):
        return self.username
