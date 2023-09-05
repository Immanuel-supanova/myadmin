from django.urls import path

from .views import HomeView, AppView, UserModelDetailView, AppModelView

app_name = 'myadmin'

urlpatterns = [
    path('', HomeView.as_view(), name='myadmin'),
    path('<slug:app>/', AppView.as_view(), name='myadmin_app'),
    path('user/<int:pk>/', UserModelDetailView.as_view(), name='user_model'),
    path('<slug:app>/<slug:model>/', AppModelView.as_view(), name='myadmin_app_model'),

]
