from django.urls import path, re_path

from . import views

urlpatterns = [
    path('log/', views.log),
    path('dockerfile/', views.get_dockerfile),
    path('access/', views.get_access),
]
