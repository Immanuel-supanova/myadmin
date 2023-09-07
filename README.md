# myadmin

This application is for monitoring Users activities in a django project.
NOTE: Only User with superuser status have access to the application 

```commandline
pip install git+https://github.com/Immanuel-supanova/myadmin.git
```

To set up the application the following settings should be implemented:

Settings.py

```
INSTALLED_APPS = [

    'myadmin',
]
```

```
# This line is very important because you need to be authenticated in order to use the app
LOGIN_URL = <set up your login url> 

```

In the root urls.py file add the following paths:
```
urlpatterns = [
    path('myadmin/', include('myadmin.urls')),
]
```
