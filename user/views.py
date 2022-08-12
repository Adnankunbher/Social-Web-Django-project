from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post,LikePost, Profile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def Post_id(request):
    if request.method=='POST':
        captions=request.POST['captions']
        image=request.FILES['img']
        user=request.user
        user=Post(captions=captions,image=image, user=user)
        user.save()

    allpost=Post.objects.all()
    data={
            'posts': allpost
        }

    return render(request,'index.html',data)

def index(request):
    new_object=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=new_object)
    return render(request,'index.html',{'user_profile':user_profile})


@login_required(login_url='/login')
def profile_info(request,username):
    getUser=User.objects.filter(username=username)
    if getUser:
        profile=Profile.objects.get(user=getUser[0])
        data={
            'profile': profile
        }
        return render(request,'profile.html',data)

    else:
        return redirect('home')


def profile(request):
    user_profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('image')==None:
            image=user_profile.profileimage
            bio=request.POST['bio']
            location=request.POST['location']
            
            user_profile.profileimage=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        if request.FILES.get('image') != None:
            image=request.FILES.get('image')
            bio=request.POST['bio']
            location=request.POST['location']
            
            user_profile.profileimage=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()

        return redirect('profile')
    return render(request,'profile.html',{'user_profile':user_profile})

@login_required(login_url='/login')
def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    messages.info(request,"Post Deleted")
    return redirect('home')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login_page')


