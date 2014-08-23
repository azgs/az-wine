from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Vineyard(models.Model):
    name = models.CharField(max_length=500, blank=True)
    owner = models.CharField(max_length=500, blank=True)
    street = models.CharField(max_length=1000, blank=True)
    county = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    description = models.TextField(max_length=350, blank=True)
    established = models.DateField(blank=True, null=True)
    website = models.URLField(max_length=300, blank=True)
    latitude = models.DecimalField(max_digits=10,
        decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10,
        decimal_places=7, blank=True, null=True)
    sunday_open = models.TimeField(blank=True, null=True)
    sunday_close = models.TimeField(blank=True, null=True)
    monday_open = models.TimeField(blank=True, null=True)
    monday_close = models.TimeField(blank=True, null=True)
    tuesday_open = models.TimeField(blank=True, null=True)
    tuesday_close = models.TimeField(blank=True, null=True)
    wednesday_open = models.TimeField(blank=True, null=True)
    wednesday_close = models.TimeField(blank=True, null=True)
    thursday_open = models.TimeField(blank=True, null=True)
    thursday_close = models.TimeField(blank=True, null=True)
    friday_open = models.TimeField(blank=True, null=True)
    friday_close = models.TimeField(blank=True, null=True)
    saturday_open = models.TimeField(blank=True, null=True)
    saturday_close = models.TimeField(blank=True, null=True)
    vineyard = models.BooleanField(default=False)
    tasting_room = models.BooleanField(default=False)
    winery = models.BooleanField(default=False)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT,
        height_field=None, width_field=None, max_length=1000,
        blank=True, null=True)

class Service(models.Model):
    vineyard_fk = models.ForeignKey(Vineyard)
    service = models.CharField(max_length=500, blank=True)
    description= models.TextField(blank=True)

class Product(models.Model):
    vineyard_fk = models.ForeignKey(Vineyard)
    product = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=100, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username