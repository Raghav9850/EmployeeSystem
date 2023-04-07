from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('', views.emp_main),
    path('list/', views.emp_list,name='emp_list'),
    path('create/',views.emp_create,name='emp_create'),
    path('update/<int:pk>',views.emp_update,name='emp_update'),
    path('delete/<int:pk>',views.emp_delete,name='emp_delete'),
    path('register/',views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    ]   