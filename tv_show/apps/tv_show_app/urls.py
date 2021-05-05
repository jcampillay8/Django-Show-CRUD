from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('home/new_show', views.new_show),
    path('home/create', views.create),
    path('home/<int:id>', views.show),
    path('home/<int:id>/edit', views.edit_show),
    path('home/<int:id>/destroy', views.destroy),
    path('home/update', views.update)
]