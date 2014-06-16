from django.contrib import admin
from azwine.models import Vineyard, Service, Product

class ServiceInline(admin.TabularInline):
	model = Service
	extra = 1

class ProductInline(admin.TabularInline):
	model = Product
	extra = 1

class VineyardAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'owner', 'description']}),
		('Contact', {'fields': ['street', 'county', 'zipcode', 
			'email', 'phone']}),
		('GeoLocation', {'fields': ['latitude', 'longitude']}),
	]
	inlines = [ServiceInline, ProductInline]

admin.site.register(Vineyard, VineyardAdmin)