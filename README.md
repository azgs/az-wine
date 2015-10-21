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
> git clone https://github.com/azgs/azwine.git
> pip install django-hijack
```
*Django-hijack allows superusers to login as and work as other users. See docs [here](https://github.com/arteria/django-hijack)*

Modify **azwineprj\azwineprj\settings.py**:
 - Add `'azwine'` to `INSTALLED_APPS`
 - `TIME_ZONE = 'America/Phoenix'`
 - `TIME_INPUT_FORMATS = ('%H:%M',)`
 - `STATIC_ROOT = os.path.join(BASE_DIR, "static")`
 - `MEDIA_ROOT = os.path.join(BASE_DIR, "media")`
 - `MEDIA_URL = '/media/'`
 - `TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'azwine/templates')]`

Also add hijack to INSTALLED_APPS:

```
INSTALLED_APPS = (
    ...,
    'hijack',
    'compat',
)
```

And add hijack redirects:

```
HIJACK_LOGIN_REDIRECT_URL = "/admin/"  # where you want to be redirected to, after hijacking the user.
REVERSE_HIJACK_LOGIN_REDIRECT_URL = "/admin/"  # where you want to be redirected to, after releasing the user.
```

Modify **azwineprj\azwineprj\ursl.py**:
 - Add `url(r'^', include('azwine.urls')),`
 - And `url(r'^hijack/', include('hijack.urls'))`

Build the database:

`> python manage.py migrate`

Create admin user:

`> python manage.py createsuperuser`

### Running for Development

```
> python manage.py makemigrations    [create migrations for database changes]
> python manage.py migrate           [apply changes to the database]
> python manage.py runserver
```

Site at [http://localhost:8000/](http://localhost:8000/) and admin site at [http://localhost:8000/admin](http://localhost:8000/admin)

### Create user group

- Log in to the admin site with the superuser account.
- Add a new group called `winegrowers`
- Give this the group the following permissions:
  - All under azwine | product
  - All under azwine | service
  - All under azwine | vineyard
  - All under azwine | user profile

### Basic Insecure Security

For a new user to set up an account they must enter the token `w1ne!` in the registration form.

### Geojson

This application creates a geojson object from the database. It is served out at [http://localhost:8000/api/rest/vineyards](http://localhost:8000/api/rest/vineyards).

### Running for Production

Modify **azwineprj\azwineprj\settings.py**:
- `DEBUG = False`
- `TEMPLATE_DEBUG = False`
- `ALLOWED_HOSTS = []`                [put host here]

### Notes on Hijaking
Hkjacking can only be as a superuser account and is entered from the buttons on the  Users page. To release a hijack go to the URL http://winedb.arizonaexperience.org/hijack/release-hijack/.