from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid

class Rider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length = 180)
    Medium = models.CharField(max_length=180)
    From_location = models.CharField(max_length=180)
    To_location = models.CharField(max_length=180)
    number_of_assets= models.IntegerField(default=0)
    Timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    def __str__(self):
        return self.id

    def __unicode__ (self) :
        return self.id
    

class Requester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length = 180)
    Phone= models.IntegerField(unique=True)
    From_location = models.CharField(max_length=180)
    To_location = models.CharField(max_length=180)
    Number_of_assets= models.IntegerField(default=0)
    Type_of_assets = models.CharField(max_length=180)
    Sensitivities = models.CharField(max_length = 180)
    Status = models.CharField(max_length=180,default="Pending")
    Timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    def __str__(self):
        return self.id
    
class RegisterRider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Requester= models.ForeignKey(Requester, on_delete=models.CASCADE, blank=True, null=True,unique=True)
    Rider= models.ForeignKey(Rider, on_delete=models.CASCADE, blank=True, null=True,unique=True)
    Timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    def __str__(self):
        return self.id
    