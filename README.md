# Arizona Wine Growers Contribute Form

The Arizona Geological Survey is building an interactive web map to support the local agricultural industry. For the sake of data integrity and long term sustainability of the program, we built this contribute form so that industry professionals can create and maintain their own data.

## Development Setup

### Prerequisites

- [Python 2.7](www.python.org)
  - In Windows remember to add Python to the PATH variable `C:\Python27\;C:\Python27\Scripts\`
- [Django 1.7](https://www.djangoproject.com/)
- Pillow - Python Imaging Library (PIL) fork
  - `> pip install pillow`
  
### Setup

```
> django-admin.py startproject azwineprj
> cd azwineprj
> git clone https://github.com/azgs/az-wine.git
```

Modify **azwineprj\azwineprj\settings.py**:
 - Add `'az-wine'` to `INSTALLED_APPS`
 - `TIME_ZONE = 'America/Phoenix'`

Modify **azwineprj\azwineprj\ursl.py**:
```
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'azwineprj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('az-wine.urls')),
)
```

Create admin user

`> python manage.py createsuperuser`

### Running for Development

```
> python manage.py migrate
> python manage.py runserver
```

Site at [http://localhost:8000/](http://localhost:8000/) and admin site at [http://localhost:8000/admin](http://localhost:8000/admin)
