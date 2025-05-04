from django.db import models
from auths.models import User
from django.contrib.auth import get_user_model

# Create your models here.
# User = get_user_model

class Employer(models.Model):
    user = models.ForeignKey(User, related_name='employers', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name