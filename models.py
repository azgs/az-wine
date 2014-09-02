from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from binascii import b2a_hex
from os import urandom

def build_uid():
    return unicode('vineyard' + b2a_hex(urandom(5)))

class Vineyard(models.Model):
    user = models.ForeignKey(User)
    vineyard_id = models.CharField(max_length=20, editable=False,
        default=build_uid)
    name = models.CharField(max_length=500, blank=True)
    owner = models.CharField(max_length=500, blank=True)
    street = models.CharField(max_length=1000, blank=True)
    county = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True,
        help_text='Please use this format: 123-456-7890')
    description = models.TextField(max_length=350, blank=True)
    established = models.DateField(blank=True, null=True,
        help_text='Please use this format: YYYY-MM-DD')
    website = models.URLField(max_length=300, blank=True)
    latitude = models.DecimalField(max_digits=10,
        decimal_places=7, blank=True, null=True,
        help_text='Please use this format: 123.4567890')
    longitude = models.DecimalField(max_digits=10,
        decimal_places=7, blank=True, null=True,
        help_text='Please use this format: 123.4567890')
    sunday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    monday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    tuesday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    wednesday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    thursday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    friday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    saturday = models.CharField(blank=True, null=True, max_length=15,
        help_text='Please use this format: 08:00AM-05:00PM')
    vineyard = models.BooleanField(default=False)
    tasting_room = models.BooleanField(default=False)
    winery = models.BooleanField(default=False)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT,
        height_field=None, width_field=None, max_length=1000,
        blank=True, null=True)

    def vineyards_serialized(self, model=None):
        if model is None:
            model = self
        json = {
            'name': model.name,
            'owner': model.owner,
            'address' : {
                'street': model.street,
                'county': model.county,
                'zipcode': model.zipcode,
            },
            'email': model.email,
            'phone': model.phone,
            'description': model.description,
            'established': model.established,
            'website': model.website,
            'geo': {
                'lat': model.latitude,
                'lng': model.longitude,
            },
            'hours': {
                'sunday': {'open': model.sunday_open,
                           'close': model.sunday_open},
                'monday': {'open': model.monday_open,
                           'close': model.monday_open},
                'tuesday': {'open': model.tuesday_open,
                           'close': model.tuesday_open},
                'wednesday': {'open': model.wednesday_open,
                           'close': model.wednesday_open},
                'thursday': {'open': model.thursday_open,
                           'close': model.thursday_open},
                'friday': {'open': model.friday_open,
                           'close': model.friday_open},
                'saturday': {'open': model.saturday_open,
                           'close': model.saturday_open},
            },
            'type': {
                'vineyard': model.vineyard,
                'tasting_room': model.tasting_room,
                'winery': model.winery
            },
#            'image': model.image,
            'services': model.get_services(model.pk),
            'products': model.get_products(model.pk),
        }
        return json

    def get_services(self, id):
        try:
            service_list = []
            services = Service.objects.filter(product_id=id)
            for s in services:
                select = {
                    'service': s.service,
                    'description': s.description
                }
                service_list.append(select)
            return service_list
        except:
            return 'undefined'

    def get_products(self, id):
        try:
            product_list = []
            products = Product.objects.filter(product_id=id)
            for p in products:
                select = {
                    'product': p.product,
                    'description': p.description
                }
                product_list.append(select)
            return product_list
        except:
            return 'undefined'

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