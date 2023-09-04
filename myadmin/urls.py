from django.urls import path

from .views import HomeView, AppView, UserModelDetailView, AppModelView

app_name = 'myadmin'

urlpatterns = [
    path('', HomeView.as_view(), name='myadmin'),
    path('<slug:app>/', AppView.as_view(), name='accounts_app'),
    path('<slug:app>/<slug:model>/', AppModelView.as_view(), name='accounts_user_model'),
    path('user/<int:pk>/', UserModelDetailView.as_view(), name='user_model')
]
