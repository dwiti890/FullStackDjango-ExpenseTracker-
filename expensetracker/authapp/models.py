from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  
    contact_number = models.CharField(max_length=15, blank=False, null=False)  

    def __str__(self):
        return f"{self.user.username} ({self.contact_number})"
