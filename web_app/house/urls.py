from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sh-home'),
    path('about/', views.about, name='sh-about'),
]
