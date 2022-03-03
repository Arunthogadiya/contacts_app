from django.db import models
from django.contrib.auth.models import User


class ContactList(models.Model):
    name=models.CharField(max_length=255)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_list')
    phone_no = models.CharField(max_length = 20)
    email=models.EmailField(max_length = 255)
    dateTime=models.DateTimeField(auto_now_add=True)