from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import  *
from django.utils.decorators import method_decorator
from django.contrib.auth.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import  Post,PostComment,User as CustUser

# Create your views here.
def Bloghome(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'user/bloghome.html',context)


def postpage(request,post_id=None):
    post = Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post)
    reply = PostComment.objects.filter(post=post).exclude(reply=False)
    context = {'post':post,'comments':comments,'reply':reply}
    return render(request,'user/post.html',context)


def postComment(request,post_id):
    if request.method == 'POST':
        if request.user.is_authenticated :
            comment = PostComment()

            comment.comment = request.POST.get('comment')
            usr = CustUser.objects.get(username=request.user)
            user = usr
            comment.user = user
            comment.post = Post.objects.get(id=post_id)
            
            reply = request.POST.get('reply')
            if reply == None:
                comment.save()
                messages.success(request,'Your Comment Added Sucessfully')
            else:
                comment.reply = True 
                com = PostComment.objects.get(sno=reply)
                par = int(com.sno)
                comment.parent = par
                comment.save()
                messages.success(request,'Your Reply Added Sucessfully')

                # Increasing Reply_Count
                com.reply_count += 1
                com.parent = 0
                com.save()

        else:
            messages.warning(request,'Please login first')
    

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(redirect_field_name='login',login_url='/user/login')
def add_post(request):
    if request.method == 'POST':
        usr = CustUser.objects.get(username=request.user)
        user = usr
        title = request.POST['title']
        text = request.POST['text']
        category = request.POST['category']

        if text == "":
            messages.warning(request, 'Please add text')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if len(text) < 150:
            messages.warning(request, 'Post must be more than 150 characters')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        


        created_at = datetime.now()
        updated_at = datetime.now()
        post = Post(user=user,title=title,category=category, text=text,created_at=created_at,updated_at=updated_at)
        post.save()
        messages.success(request,'Your Post added sucessfully')
        return redirect('bloghome')
    
    return render(request,'user/add_post.html')

def dashboard(request):
    usr = CustUser.objects.get(username=request.user)
    posts = Post.objects.filter(user=usr)
    context = {'posts':posts}
    return render(request,'user/dashboard.html',context)

def signup(request):
    users = User.objects.all()

    if request.method == 'POST':
        # Get the post paramters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        for i in users:
          if  username == i.username:
              messages.error(request, "Username already taken choose different username ")
              return HttpResponseRedirect(request.META.get('HTTP_REFERER')) ## return to same page
        
        # Check for errorneous inputs
        # username should be under 10 character
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) ## return to same page
        
        # username should be lowercase
        if not username.islower():
            messages.error(request, "Username should in lowercase")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) ## return to same page

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) ## return to same page

        # password should match
        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) ## return to same page


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        usr = CustUser(username=username,first_name=fname,last_name=lname,email=email,password=pass1)

        usr.save()

        messages.success(request,'Your  account has been successfully created')
        return redirect('login') ## return to same page 

    else:
        return render(request,'user/signup.html')


def userlogin(request):
    if request.method == 'POST':
        # Get the post paramters
        uname = request.POST['username']
        pass1 = request.POST['pass1']

        
                   
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('bloghome')

        else:
            messages.error(request, "Invalid Crendentials, Please try again")
            return redirect('login')
    else:
        return render(request,'user/login.html')

def userlogout(request):
    logout(request)
    messages.success(request,'User Logout successfully')
    return redirect('bloghome')

class MyPasswordChangeView(PasswordChangeView):
    template_name='user/changepass.html'
   
    
class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name='user/password_change_done.html'
    
class MyPasswordResetView(PasswordResetView):
    template_name='user/password_reset.html'
    
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='user/password_reset_done.html'
    
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='user/password_reset_confirm.html'
    
class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='user/password_reset_complete.html'
