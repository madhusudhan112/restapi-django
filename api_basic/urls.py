from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('detail/<int:id>/', views.todoDetail, name='detail'),
    path('create', views.todoCreate, name='create'),
    path('update/<int:id>/', views.todoUpdate, name='update'),
    path('delete/<int:id>/', views.todoDelete, name='delete'),
]
