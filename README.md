# myadmin

This application is for monitoring Users activities in a django project

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

In the root urls.py file add the following paths:
```
urlpatterns = [
    path('myadmin/', include('myadmin.urls')),
]
```
