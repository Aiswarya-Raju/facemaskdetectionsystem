from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('social/', views.social, name = 'social'),
    path('sanitizer/', views.sanitizer, name = 'sanitizer'),
    path('mask/', views.mask, name = 'mask'),
    path('payment/', views.payment, name = 'payment'),
]
