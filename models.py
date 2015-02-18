from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from binascii import b2a_hex
from os import urandom
from django.core.validators import MinValueValidator, MaxValueValidator

def build_uid():
    return unicode('vineyard' + b2a_hex(urandom(5)))

class Vineyard(models.Model):
    user = models.ForeignKey(User)
    vineyard_id = models.CharField(max_length=20, editable=False, default=build_uid)
    name = models.CharField(max_length=64)
    owner = models.CharField(max_length=64, blank=True)
    street = models.CharField(max_length=64, blank=True)
    county = models.CharField(max_length=64, blank=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True)
    phone = models.CharField(max_length=12, blank=True, help_text='Please use this format: 123-456-7890')
    description = models.TextField(max_length=1000, blank=True)
    established = models.DateField(blank=True, null=True, help_text='Please use this format: YYYY-MM-DD')
    website = models.URLField(max_length=256, blank=True)
    latitude = models.DecimalField(validators=[MinValueValidator(31.3322), MaxValueValidator(37.0009)], max_digits=10, decimal_places=7, blank=False, null=True, help_text='For Arizona locations this value needs to be between 31.3322 and 37.0009.')
    longitude = models.DecimalField(validators=[MinValueValidator(-114.8387), MaxValueValidator(-109.0463)], max_digits=10, decimal_places=7, blank=False, null=True, help_text='For Arizona locations this value needs to be between -114.8387 and -109.0463.')
    sun_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    sun_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    sun_call = models.BooleanField('call/by appointment', default=False)
    mon_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    mon_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    mon_call = models.BooleanField('call/by appointment', default=False)
    tue_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    tue_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    tue_call = models.BooleanField('call/by appointment', default=False)
    wed_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    wed_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    wed_call = models.BooleanField('call/by appointment', default=False)
    thur_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    thur_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    thur_call = models.BooleanField('call/by appointment', default=False)
    fri_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    fri_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    fri_call = models.BooleanField('call/by appointment', default=False)
    sat_open_time = models.TimeField('open', null=True, blank=True, help_text='Use 24 hour format.')
    sat_close_time = models.TimeField('close', null=True, blank=True, help_text='Use 24 hour format.')
    sat_call = models.BooleanField('call/by appointment', default=False)
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
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(model.longitude), float(model.latitude)]
            },
            "properties": {
                "name": model.name,
                "uid":  model.id,
                "owner": model.owner,
                "address" :{
                    "street": model.street,
                    "county": model.county,
                    "zipcode": model.zipcode,
                },
                "email": model.email,
                "phone": model.phone,
                "description": model.description,
                "established": str(model.established),
                "website": model.website,
                "services": model.get_services(model.id),
                "products": model.get_products(model.id),
                "hours":{
                    "sunday": {
                        "open": str(model.sun_open_time),
                        "close": str(model.sun_close_time),
                        "call": model.sun_call,
                    },
                    "monday": {
                        "open": str(model.mon_open_time),
                        "close": str(model.mon_close_time),
                        "call": model.mon_call,
                    },
                    "tuesday": {
                        "open": str(model.tue_open_time),
                        "close": str(model.tue_close_time),
                        "call": model.tue_call,
                    },
                    "wednesday": {
                        "open": str(model.wed_open_time),
                        "close": str(model.wed_close_time),
                        "call": model.wed_call,
                    },
                    "thursday": {
                        "open": str(model.thur_open_time),
                        "close": str(model.thur_close_time),
                        "call": model.thur_call,
                    },
                    "friday": {
                        "open": str(model.fri_open_time),
                        "close": str(model.fri_close_time),
                        "call": model.fri_call
                    },
                    "saturday": {
                        "open": str(model.sat_open_time),
                        "close": str(model.sat_close_time),
                        "call": model.sat_call,
                    },
                },
                "type": {
                    "vineyard": model.vineyard,
                    "tasting_room": model.tasting_room,
                    "winery": model.winery
                }
            }
        }
        return json

    def get_services(self, vid):
        try:
            service_list = []
            services = Service.objects.filter(vineyard_fk=vid)
            for s in services:
                select = {
                    'service': s.service,
                    'description': s.description
                }
                service_list.append(select)
            return service_list
        except:
            return 'undefined'

    def get_products(self, vid):
        try:
            product_list = []
            products = Product.objects.filter(vineyard_fk=vid)
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
    service = models.CharField(max_length=100, blank=True)
    description= models.TextField(max_length=500, blank=True)

class Product(models.Model):
    vineyard_fk = models.ForeignKey(Vineyard)
    product = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=350, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username