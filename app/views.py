from django.shortcuts import redirect, render
from django.views import View
from .models import BlogPost
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Hoepage Views
class Index(View):
    def get(self,request):
        posts = BlogPost.objects.all()
        return render(request,'index.html',{'posts':posts})

# About Views
def about(request):
    return render(request,'about.html')

# Dashboard Views
def dashboard(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.filter(author = request.user)
        return render(request,'dashboard.html',{'posts':posts})
    else:
        redirect('login')

# signup Views
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation!! You have become an Author')
            form.save()
            form.clean()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

# Login Views
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username= uname,password = upass)
                login(request,user)
                print("User logged inf")
                messages.success(request,'Logged in Successfully !!')
                return redirect('dashboard')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('dashboard')

# Logut Views
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homepage')
    else:
        return redirect('login')
    
# Add Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                blog_post = BlogPost(
                    title = form.cleaned_data['title'],
                    content = form.cleaned_data['content'],
                    author = request.user
                )
                blog_post.save()
                messages.success(request,'Post added Successfully !!')
                return redirect('dashboard')
        else:
            form = PostForm()
            return render(request , 'add_post.html',{'form':form})
    else:
        return redirect('login')

# Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = BlogPost.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'Post Updated Successfully !!')
                return redirect('dashboard')
        else:
            pi = BlogPost.objects.get(pk=id)
            form = PostForm(instance=pi)
            return render(request , 'update_post.html',{'form':form})
    else:
        return redirect('login')
    
# delete_post
def delete_post(request,id):
    if request.user.is_authenticated:
        pi = BlogPost.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Post has been deleted!!')
        return redirect('dashboard')
    else:
        return redirect('login')
  