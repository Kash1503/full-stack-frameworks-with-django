from django.db import models
from tickets.models import Ticket

# Create your models here.
class Order(models.Model):
    """
    Take informaion from the customer to create an order
    """

    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=20, blank=False)
    county = models.CharField(max_length=30, blank=False)
    town_or_city = models.CharField(max_length=30, blank=False)
    postcode = models.CharField(max_length=15, blank=True)
    street1 = models.CharField(max_length=50, blank=False)
    street2 = models.CharField(max_length=50, blank=False)
    date_ordered = models.DateField()

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.id, self.date_ordered, self.full_name)


class OrderLineItem(models.Model):
    """Store information about the order, ticket which was supported and the amount pledged"""

    order = models.ForeignKey(Order, null=False, on_delete=models.PROTECT)
    ticket = models.ForeignKey(Ticket, null=False, on_delete=models.PROTECT)
    pledge = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} for {1}'.format(self.pledge, self.ticket.title)