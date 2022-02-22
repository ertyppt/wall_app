from django.urls import path
from wallsystem import views

urlpatterns = [
    path('wall/', views.wall_list),
]