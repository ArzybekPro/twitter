from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.users.models import User,Followers
from apps.posts.models import Post,Comment,Like,Chat,Message
from apps.settings.models import Settings
from django.db.models import Q
# Create your views here.

def register(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        profile_image = request.FILES.get('profile_image')
        gender = request.POST.get('gender')
        if password == confirm_password:
            try:
                user = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email, phone_number = phone_number, profile_image = profile_image, gender = gender)
                user.set_password(password)
                user.save()       
                user = User.objects.get(username = username)
                user =authenticate(username = username ,password = password)
                login(request ,user)
                
                return redirect('account_settings',user.username)
            except:
                return redirect('register')
    context = {
        'settings':settings
    }
    return render(request, 'users/form-register.html', context)

def user_login(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = User.objects.get(username=username)
        user =authenticate(username=username ,password=password)
        login(request,user)     
            
        return redirect('index')
    context ={
        'settings':settings
    }
    return render (request ,'users/form-login.html' ,context)


def account(request,username):
    settings = Settings.objects.latest('id')
    user = User.objects.get(username=username)
    follow_status = Followers.objects.filter(from_user = request.user, to_user = user).exists()
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
        if 'comment' in request.POST:
            text= request.POST.get('text')
            post= request.POST.get('post')
            try:
                comment = Comment.objects.create(post_id= post, user = request.user,text = text)
                comment.save()
            except:
                return redirect('index')
        
        if 'follow' in request.POST:
            try:
                follow = Followers.objects.get(to_user=user, from_user = request.user )
                follow.delete()
                return redirect('account', user.username)
            except:
                follow = Followers.objects.create(to_user=user, from_user = request.user)
                return redirect('account', user.username)
    context={
        'user':user,
        'settings':settings,
        'follow_status':follow_status,
    }
    return render(request,'users/account.html',context)

def account_settings(request,username):
    settings = Settings.objects.latest('id')
    user=User.objects.get(username=username)
    if request.user != user:
        return redirect('index')
    if request.method == 'POST':
        gender=request.POST.get('gender')
        phone_number=request.POST.get('phone_number')
        live_in=request.POST.get('live_in')
        from_in=request.POST.get('from_in')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        relationship=request.POST.get('relationship')
        profile_image=request.FILES.get('profile_image')
        try:
            user.gender = gender
            user.phone_number = phone_number
            user.live_in = live_in
            user.from_in = from_in
            user.first_name = first_name
            user.profile_image = profile_image
            user.last_name = last_name
            user.relationship = relationship
            user.save()
        except:
            return redirect('account_settings')
    context={
        'user':user,
        'settings':settings
        
    }
    return render(request,'users/account_settings.html', context)


def chats(request,id):
    user=User.objects.get(id=id)
    all_chats = Chat.objects.all().filter(Q(from_user = user ) | Q(to_user = user))
    context={
        'all_chats':all_chats
    }
    return render(request , 'users/chats-friend.html' ,context)


def chat_detail(request,id, username):
    chat = Chat.objects.get(id = id)
    user = User.objects.get(username = username)
    all_chats = Chat.objects.all().filter(Q(from_user=user) | Q(to_user=user))
    if request.method == 'POST':
        if 'message' in request.POST:
            text= request.POST.get('text')
            try:
                message = Message.objects.create(from_user =request.user,chat=chat,message=text)
                message.save()
                return redirect('chat_detail',chat.id, user.username)
            except:
                return redirect('chat_detail',chat.id, user.username)
        if 'delete_chat' in request.POST:
            for i in chat.message_chat.all():
                i.delete()
            return redirect('chat_detail',chat.id, user.username)

        
    context={
        'chat':chat,
        'all_chats':all_chats,
  
    }
    return render(request,'users/chat_detail.html',context)