from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  
    contact_number= models.CharField(max_length=15, blank=False, null=False)  # Additional validation recommended
    def _str_(self):
        return f"{self.name} ({self.register_number})"