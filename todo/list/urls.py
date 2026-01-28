from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('task',views.task,name="task"),
    path('login',views.logged_in,name="logged_in"),
    path('register',views.register,name="register"),
    path('logout',views.logout_user,name="logout_user"),
    path('task_update/<int:id>',views.task_update,name="task_update"),
    path('task_complete/<int:id>',views.task_complete,name="task_complete"),
    path('task_delete/<int:id>',views.task_delete,name="task_delete"),
]