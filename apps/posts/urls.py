from django.urls import path
from apps.posts.views import update_post,post_delete,comment_delete,search,todolist,aboutTodo

urlpatterns = [
    path('update_post/<int:id>/' , update_post,name='update_post'),
    path('post_delete/<int:id>/',post_delete,name='post_delete'),
    path('comment_delete/<int:id>/',comment_delete,name = 'comment_delete'),
    path('search/' , search ,name='search'),
    path('todolist/',todolist,name='todolist'),
    path('aboutTodo/',aboutTodo,name = 'aboutTodo')
]
