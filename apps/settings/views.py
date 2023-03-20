from django.shortcuts import render,redirect
from apps.settings.models import Settings
from apps.posts.models import Post,Videos,Like,Comment,LikeComment,Chat

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    posts= Post.objects.all().order_by('-id')

    if request.method == 'POST':
        if 'create_post' in request.POST:
            post_text=request.POST.get('post_text')
            post_file=request.FILES.get('post_file')
            if post_file:
                try:
                    post=Post.objects.create(image=post_file,user=request.user)
                    post.save()
                except:
                    post=Post.objects.create(video=post_video,user=request.user)
                    post.save()
                
            else:
                post=Post.objects.create(text=post_text,user=request.user)
                post.save()
                
        if 'like' in request.POST:
            post = request.POST.get('post')
            try:
                like = Like.objects.get(user = request.user,post_id=post)
                like.delete()
                return redirect('index')
            except:
                like=Like.objects.create(user=request.user, post_id = post)
                return redirect('index')
            
        if 'like_comment' in request.POST:
            like_comment_id= request.POST.get('like_comment_id')
            try:
                like_comment = LikeComment.objects.get(user = request.user,comment_id = like_comment_id)
                like_comment.delete()
                return redirect('index')
            except:
                like_comment = LikeComment.objects.create(user=request.user , comment_id = like_comment_id)
                return redirect('index')
            
        if 'comment' in request.POST:
            text= request.POST.get('text')
            post= request.POST.get('post')
            try:
                comment = Comment.objects.create(post_id= post, user = request.user,text = text)
                comment.save()
            except:
                 return redirect('index')
        if 'create_chat' in request.POST:
            to_user = request.POST.get('to_user')
            try:
                try:
                    chat = Chat.objects.get(from_user = request.user , to_user_id = to_user)
                    return redirect('chat_detail',chat.id, request.user.username)
                except:
                    chat = Chat.objects.get(to_user = request.user , from_user_id = to_user)
                    return redirect('chat_detail',chat.id, request.user.username)
            except:
                chat = Chat.objects.create(from_user = request.user , to_user_id = to_user)
                chat.save()
                return redirect('chat_detail',chat.id, request.user.username)
        
        # if 'chat_delete' in request.POST:
        #     to_user = request.POST.get('to_user')
        #     try
    context ={
        'settings':settings,
        'posts':posts
    }
    return render(request,'feed.html' , context)

def video_index(request):
    videos= Videos.objects.all()
    context={
        'videos':videos
    }
    return render(request ,'videos.html' ,context)

