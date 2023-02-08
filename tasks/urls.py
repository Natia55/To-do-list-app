from django.urls import path
from . views import list_tasks, create_tasks, delete_tasks, update_tasks


urlpatterns = [
    path('', list_tasks, name='list_tasks'),
    path('create/', create_tasks, name='create_tasks'),
    path('<int:pk>/delete/', delete_tasks, name='delete_tasks'),
    path('<int:pk>/update/', update_tasks, name='update_tasks'),

]
