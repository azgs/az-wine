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

    def get_queryset(self, request):
        user = request.user
        method = getattr(super(FilterUserAdmin, self), 'get_queryset', super(FilterUserAdmin, self).queryset)
        qs = method(request)
        if user.is_superuser:
            return qs.all()
        else:
            return qs.filter(user=request.user)

    # Allow queryset method as fallback for Django versions < 1.6
    # for versions >= 1.6 this is taken care of by Django itself
    # and triggers a warning message automatically.
    import django
    if django.VERSION < (1, 6):
        queryset = get_queryset

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
        ('Sunday Hours of Operation', {'fields': [
            'sun_open_time', 'sun_close_time', 'sun_call']}),
        ('Monday Hours of Operation', {'fields': [
            'mon_open_time', 'mon_close_time', 'mon_call']}),
        ('Tuesday Hours of Operation', {'fields': [
            'tue_open_time', 'tue_close_time', 'tue_call']}),
        ('Wednesday Hours of Operation', {'fields': [
            'wed_open_time', 'wed_close_time', 'wed_call']}),
        ('Thursday Hours of Operation', {'fields': [
            'thur_open_time', 'thur_close_time', 'thur_call']}),
        ('Friday Hours of Operation', {'fields': [
            'fri_open_time', 'fri_close_time', 'fri_call']}),
        ('Saturday Hours of Operation', {'fields': [
            'sat_open_time', 'sat_close_time', 'sat_call']}),
        ('Type of business (select all that apply)', {'fields': ['vineyard',
            'tasting_room', 'winery']})
    ]
    inlines = [ServiceInline, ProductInline]
    list_display = ('name', 'owner', 'county', 'zipcode', 'established')

admin.site.register(Vineyard, VineyardAdmin)
