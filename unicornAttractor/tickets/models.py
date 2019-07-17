from django.db import models
from django.utils import timezone
from django.contrib import auth

# Create your models here.

class Ticket(models.Model):
    """Model to store ticket information"""

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    upvotes = models.IntegerField(default=0, null=False)
    views = models.IntegerField(default=0, null=False)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey('auth.User', null=False, on_delete=models.SET_DEFAULT, default=1)
    status = models.CharField(max_length=200, null=False, default='reviewing')
    lastUpdatedBy = models.CharField(max_length=200, null=False, default='unknown')
    lastUpdatedDateTime = models.DateTimeField()
    value = models.FloatField(default=0)
    ticket_type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title   


class Comments(models.Model):
    """Model to store user comments"""

    userID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(null=False, default='')
    upvotes = models.IntegerField(default=0, null=False)
    ticketID = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID: {0} - User: {1} - Ticket: {2}'.format(self.id, self.userID.username, self.ticketID.id)