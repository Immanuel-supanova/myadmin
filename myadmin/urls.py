from django.urls import path

from .views import HomeView

app_name = 'myadmin'

urlpatterns = [
    path('', HomeView.as_view(), name='myadmin')
]
