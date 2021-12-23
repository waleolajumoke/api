from django.urls import path 
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-task', views.createtask, name='create-task'),
    path('alltask', views.alltask, name='alltask'),
    path('delete-task/<int:id>', views.deletetask, name='delete-task'),
    path('edit-task/<int:id>', views.edittask, name='edit-task'),
]

