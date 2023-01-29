from django.urls import path
from app1.views import *
app_name='nandu'
urlpatterns = [
    path('aishu/',aishu,name='aishu')
]
