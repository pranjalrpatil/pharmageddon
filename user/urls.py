from django.contrib import admin
from django.urls import path
from .views import   RegisterAPI,LoginUserView
from django.urls import path
from knox import views as knox_views
#from .views import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('accounts/login/', LoginUserView.as_view(), name='login'),
   # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
   # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]