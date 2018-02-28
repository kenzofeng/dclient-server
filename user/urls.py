from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.get_pwd),
    path('log/', views.log),
    path('dockerfile/', views.get_dockerfile),
]