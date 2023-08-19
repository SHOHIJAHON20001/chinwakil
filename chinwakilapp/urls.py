from django.urls import path
from chinwakilapp.views import home


app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
]