from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from hips import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/',include('home.urls')),
    path('login/home/bruh',views.bruh)
]