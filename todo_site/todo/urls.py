from django.urls import path
from .views import ToDoList,ToDoGet,ToDoCreate,ToDoUpdate,ToDoDelete
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

urlpatterns=[
    path('todo/',ToDoList.as_view(),name='todo-list'),
    path('token/',token_obtain_pair),
    path('token/refresh/',token_refresh),
    path('todo/<int:pk>/',ToDoGet.as_view()),
    path('todo-create/',ToDoCreate.as_view()),
    path('todo-update/<int:pk>/',ToDoUpdate.as_view()),
    path('todo-delete/<int:pk>/',ToDoDelete.as_view())
]