from django.db import models
from django.utils import timezone

# Create your models here.

class Ticket(models.Model):
    """Model to store ticket information"""

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    upvotes = models.IntegerField(default=0, null=False)
    views = models.IntegerField(default=0, null=False)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    userID = models.IntegerField(null=False, default=0)
    status = models.CharField(max_length=200, null=False, default='under review')
    lastUpdatedByID = models.IntegerField(null=False, default=0)
    lastUpdatedDateTime = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_type = models.CharField(max_length=50, null=False, default='bug')

    def __str__(self):
        return self.title   