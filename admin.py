from django.contrib import admin
from models import Vineyard, Service, Product

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    max_num = 3

class FilterUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        user = request.user
        if user.is_superuser:
            qs = super(FilterUserAdmin, self).queryset(request)
            return qs.all()
        else:
            qs = super(FilterUserAdmin, self).queryset(request)
            return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if obj.user.is_superuser:
            return True
        else:
            return obj.user

class VineyardAdmin(FilterUserAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'owner', 'description',
            'established', 'website', 'image']}),
        ('Contact', {'fields': ['street', 'county', 'zipcode',
            'email', 'phone']}),
        ('GeoLocation', {'fields': ['latitude', 'longitude']}),
        ('Hours of Operation', {'fields': ['sunday', 'monday', 'tuesday',
            'wednesday', 'thursday', 'friday', 'saturday']}),
        ('Type of business (select all that apply)', {'fields': ['vineyard',
            'tasting_room', 'winery']})
    ]
    inlines = [ServiceInline, ProductInline]
    list_display = ('name', 'owner', 'county', 'zipcode')

admin.site.register(Vineyard, VineyardAdmin)