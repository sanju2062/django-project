from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    contact_no = models.IntegerField(max_length=10,null=True)
    email_id = models.CharField(max_length=20,null=True)
    company = models.TextField(null=True)