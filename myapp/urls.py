from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('build-resume/', views.build_resume, name='build_resume'),
    path('demo-templates/', views.demo_templates, name='demo_templates'),
    path('download_template/<str:template_name>/', views.download_template, name='download_template'),
    path('user-resume/<str:username>', views.user_resume, name='user_resume'),
]