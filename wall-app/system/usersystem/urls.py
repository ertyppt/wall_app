from django.urls import path
from usersystem import views

urlpatterns = [
    path('users/', views.user_list),
]