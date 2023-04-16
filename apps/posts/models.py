from django.db import models
from apps.users.models import User

# Create your models here.

class Post(models.Model):
    text=models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    video=models.FileField(
        upload_to='post_video/',
        blank=True,
        null=True
    )
    image=models.ImageField(
        upload_to='post_image/',
        blank=True,
        null=True
    )
    user=models.ForeignKey(
        User,
        related_name='user_post',
        on_delete=models.CASCADE
    )
    
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name='post',
        verbose_name_plural='posts'

class Videos(models.Model):
    title=models.CharField(
        max_length=50
    )
    description=models.TextField(
        max_length=200
    )
    time_of =models.DateField(
        auto_now_add=True
    )
    video_file=models.FileField(
        upload_to='post_video/',
    )
    poster = models.ImageField(
        upload_to='post_poster/',
    )
    user = models.ForeignKey(
        User,
        related_name='user_video',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Видео'
        verbose_name_plural='Видео'
    
    
class Like(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='like_post',
        on_delete=models.CASCADE

    )
    user=models.ForeignKey(
        User,
        related_name='like_post',
        on_delete=models.CASCADE
    )
class Comment(models.Model):
    post=models.ForeignKey(
        Post,
        related_name='comment_post',  
        on_delete=models.CASCADE           
    )
    user= models.ForeignKey(
    User,
    related_name='comment_user',  
    on_delete=models.CASCADE                
    )
    text= models.CharField(
        max_length=255
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    
class LikeComment(models.Model):
    comment = models.ForeignKey(
        Comment, 
        related_name='like_comment',
        on_delete=models.CASCADE,
        
        )
    
    user = models.ForeignKey(
        User, 
        related_name='like_comment',
        on_delete=models.CASCADE,
        )

class Chat(models.Model):
    from_user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='from_user',
        verbose_name='Чат пользователя'
        )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user',
        verbose_name='Чат к пользователя',
        )

    class Meta:
        verbose_name="Чат"
        verbose_name_plural="Чаты"

class Message(models.Model):
    chat=models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='message_chat',
        verbose_name='ID чата'
    )
    from_user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_from_user',
        verbose_name="Сообщение от пользователя",
        )
    message=models.CharField(
        max_length=200,
        verbose_name='Сообщение'
    )
    created_at=models.TimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"{self.chat}"
    
    class Meta:
        verbose_name= "Сообщение в чате",
        verbose_name_plural= "Сообщение в чатах"


class Task(models.Model):
    Priority = (('L', 'Low'),
                ('M', 'Medium'),
                ('H', 'High'))
    task_name = models.CharField(
        max_length=50
    )
    du_date = models.DateTimeField(
        default=None, null=True ,blank = True
    )
    
    complated = models.BooleanField(
        default=False
    )
    priority = models.CharField(max_length =1,choices=Priority , default = 'L')
    
    def __str__(self):
        return self.task_title
    