from django.urls import path
from test1 import views

app_name = 'rents'

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.index_base, name='index_base'),
    path('testget/', views.testget, name='testget')
] 