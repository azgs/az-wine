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
 - Add `url(r'^', include('az-wine.urls')),`

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
