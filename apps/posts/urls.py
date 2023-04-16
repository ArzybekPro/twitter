from django.urls import path
from apps.posts.views import update_post,post_delete,comment_delete,search,home,completed,delete,filter_priority,filter_status

urlpatterns = [
    path('update_post/<int:id>/' , update_post,name='update_post'),
    path('post_delete/<int:id>/',post_delete,name='post_delete'),
    path('comment_delete/<int:id>/',comment_delete,name = 'comment_delete'),
    path('search/' , search ,name='search'),
    path('home/',home,name='home'),
    path('completed/<int:id>/',completed,name='completed'),
    path('delete/<int:id>/',delete,name='delete'),
    path('filter/choice/',filter_priority,name='priority'),
    path('status/choice/',filter_status,name='status'),
]
