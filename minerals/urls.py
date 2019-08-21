from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    path('<int:id>', views.mineral_detail, name='detail'),
]