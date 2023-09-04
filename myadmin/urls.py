from django.urls import path

from .views import HomeView, AccountAppView, UserModelDetailView, UserModelView

app_name = 'myadmin'

urlpatterns = [
    path('', HomeView.as_view(), name='myadmin'),
    path('accounts/', AccountAppView.as_view(), name='accounts_app'),
    path('accounts/user/', UserModelView.as_view(), name='accounts_user_model'),
    path('user/<int:pk>/', UserModelDetailView.as_view(), name='user_model')
]
