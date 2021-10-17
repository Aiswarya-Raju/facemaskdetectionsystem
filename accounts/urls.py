from django.urls import path

from . import views
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

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
    path('end/', views.end, name = 'end'),
     path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
