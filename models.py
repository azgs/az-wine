from django.db import models

class Vineyard(models.Model):
	name = models.CharField(max_length=500, blank=True)
	owner = models.CharField(max_length=500, blank=True)
	street = models.CharField(max_length=1000, blank=True)
	county = models.CharField(max_length=100, blank=True)
	zipcode = models.IntegerField()
	email = models.EmailField(max_length=200, blank=True)
	phone = models.CharField(max_length=12, blank=True)
	description = models.TextField(blank=True)
	latitude = models.DecimalField(max_digits=10, 
		decimal_places=10, blank=True)
	longitude = models.DecimalField(max_digits=10, 
		decimal_places=10, blank=True)

class Service(models.Model):
	vineyard = models.ForeignKey(Vineyard)
	service = models.CharField(max_length=500, blank=True)
	description= models.TextField(blank=True)

class Product(models.Model):
	vineyard = models.ForeignKey(Vineyard)
	product = models.CharField(max_length=500, blank=True)
	description = models.TextField(blank=True)