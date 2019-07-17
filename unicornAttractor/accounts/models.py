from django.db import models

# Create your models here.
class UserProfile(models.Model):
    """
    Store further information for each user
    """

    phone_number = models.CharField(max_length=30, blank=True, default='')
    country = models.CharField(max_length=20, blank=True, default='')
    county = models.CharField(max_length=30, blank=True, default='')
    town_or_city = models.CharField(max_length=30, blank=True, default='')
    postcode = models.CharField(max_length=15, blank=True, default='')
    street1 = models.CharField(max_length=50, blank=True, default='')
    street2 = models.CharField(max_length=50, blank=True, default='')
    userID = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}  -  {1}'.format(self.id, self.userID.username)