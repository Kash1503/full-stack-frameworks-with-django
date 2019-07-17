from django.db import models

# Create your models here.
class UserProfile(models.Model):
    """
    Store further information for each user
    """

    phone_number = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)
    county = models.CharField(max_length=30, blank=True)
    town_or_city = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=15, blank=True)
    street1 = models.CharField(max_length=50, blank=True)
    street2 = models.CharField(max_length=50, blank=True)
    userID = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}  -  {1}'.format(self.id, self.userID.username)