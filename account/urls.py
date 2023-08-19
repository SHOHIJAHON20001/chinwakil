from django.urls import path
from .  import views

app_name = 'account'
urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('logout_page/', views.logout_page, name='logout_page'),
]