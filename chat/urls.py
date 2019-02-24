from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<str:room_name>/', views.room, name='room'),
]
