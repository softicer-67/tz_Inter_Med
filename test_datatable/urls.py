from django.urls import path
from . import views
from .views import ListDataVew

urlpatterns = [
    path('init_db/', views.init_db, name='init_db'),
    path('', ListDataVew.as_view(), name='data_list'),
]
