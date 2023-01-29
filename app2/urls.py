from django.urls import path
from app2.views import *
app_name='geetha'
urlpatterns = [
    path('dubbi/',dubbii,name='dubbii')
]

