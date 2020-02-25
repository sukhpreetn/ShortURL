from django.urls import path
from . import views


app_name = 'Shortener'

urlpatterns = [
    path('<str:token>', views.home, name = 'home'),
    path('', views.index, name = 'index'),
    path('stats/', views.stats, name='stats'),

]