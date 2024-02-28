from django.urls import path
from .views import home, blogpost_create, blogpost_update, blogpost_delete
from django.urls import path
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('create/', blogpost_create, name='blogpost_create'),
    path('update/<int:pk>/', blogpost_update, name='blogpost_update'),
    path('delete/<int:pk>/', blogpost_delete, name='blogpost_delete'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('category/', views.category, name='category'),

]
