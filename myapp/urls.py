from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('build-resume/', views.build_resume, name='build_resume'),
    path('demo-templates/', views.demo_templates, name='demo_templates'),
]