from django.contrib import admin
from apps.posts.models import Post, Videos, Chat, Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name']


admin.site.register(Post)
admin.site.register(Videos)
admin.site.register(Chat)
admin.site.register(Task, TaskAdmin)
