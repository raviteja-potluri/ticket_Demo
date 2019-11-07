from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserObjects(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "userobjects"
        unique_together = ('username', 'password')

class TicketDetails(models.Model):
    ticketid = models.AutoField(primary_key=True)
    userobjects = models.ForeignKey(UserObjects, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    ticket_desc = models.CharField(max_length=128)
    notes = models.CharField(max_length=128,default ="")
    ticket_category = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "ticketdetails"

class NotesDetails(models.Model):
    notesid = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(TicketDetails, on_delete=models.CASCADE)
    notes = models.CharField(max_length=128)
    userobjects = models.ForeignKey(UserObjects, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "notesdetails"
from django.db import models

# Create your models here.
