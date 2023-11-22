from django.contrib import admin
from django.urls import path,include
from todo import urls

from .import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name = "home"),
    path("login/",views.loginn,name="login"),
    path("signup/",views.signupp,name="signupp"),
    path("logout/",views.logoutt,name="logoutt"),
    path("tasks/",views.tasks,name= "tasks"),
    path('profile/',views.profile,name = "profile"),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('completed/<int:message_id>/', views.completed, name='completed'),

    
]
