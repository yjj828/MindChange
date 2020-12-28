from django.urls import path
from thoughtReverse import views

app_name = 'thoughtReverse'

urlpatterns = [
    path('', views.index, name='index'),
]