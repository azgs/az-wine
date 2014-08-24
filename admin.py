from django.contrib import admin
from models import Vineyard, Service, Product, UserProfile

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    max_num = 3

class VineyardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'owner', 'description',
            'established', 'website', 'image']}),
        ('Contact', {'fields': ['street', 'county', 'zipcode',
            'email', 'phone']}),
        ('GeoLocation', {'fields': ['latitude', 'longitude']}),
        ('Hours of Operation', {'fields': ['sunday_open', 'sunday_close',
            'monday_open', 'monday_close', 'tuesday_open', 'tuesday_close',
            'wednesday_open', 'wednesday_close', 'thursday_open',
            'thursday_close', 'friday_open', 'friday_close', 'saturday_open',
            'saturday_close']}),
        ('Type of business (select all that apply)', {'fields': ['vineyard',
            'tasting_room', 'winery']})
    ]
    inlines = [ServiceInline, ProductInline]
    list_display = ('name', 'owner', 'county', 'zipcode')

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        qs = super(VineyardAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Vineyard, VineyardAdmin)