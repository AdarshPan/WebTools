from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views import generic
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def Index(request):
    tc=timezone.now()
    message='Welcome'
    # if float(tc)>=12.0:
    #     message='GoodAfternoon'
    # else:
    #     message="GoodMorning"



    return render(request,'ctgctg/index.html',{'message':message})

def Register(request):
    registered=False
    form=forms.UserForm()
    user_info_form=forms.UserInfoForm()
    user_login_form_register=forms.UserLoginForm()
    if request.method=="POST":
        form=forms.UserForm(request.POST)
        user_info_form=forms.UserInfoForm(request.POST)
        if form.is_valid() and user_info_form.is_valid():
            form1=forms.UserForm(request.POST).save(commit=False)
            user_info_form=forms.UserInfoForm(request.POST).save(commit=False)
            # form.username=form.cleaned_data['username']
            # form.block=form.cleaned_data['block']

            form1.set_password(form1.password)

            form1.save()

            user_info_form.username = form1
            user_info_form.save()
            registered=True

            # form.intercom_number=form.cleaned_data['intercom_number']
            # form.flat_number=form.cleaned_data['flat_number']
            #return HttpResponse("Registered")
            return render(request,'ctgctg/registration.html',{'login_form':user_login_form_register,"registered":registered})
    return render(request,'ctgctg/registration.html',{"form":form,'user_info_form':user_info_form})
def user_login(request):
   user_login_form=forms.UserLoginForm()
   if request.method=="POST":
       user_login_form=forms.UserLoginForm(data=request.POST)
       if user_login_form.is_valid():
           username=request.POST.get('username')
           password=request.POST.get('password')
           user=authenticate(username=username,password=password)
           if user:
             if user.is_active:
               login(request,user)
               return render(request,'ctgctg/index.html')
               # return reverse_lazy('ctgctg/insidepage.html')
             else:
                 return HttpResponse("USER IS INACTIVE")
               # return render (request,'ctgctg/insidepage.html')
           else:
             return HttpResponse("HEY GO AND REGISTER FIRST")
       else:
           return HttpResponse("Invalid Form")
   else:
       return render(request,'ctgctg/login.html',{'login_form':user_login_form})
# @login_required
# def PlayGame(request):
#     return render(request,'ctgctg/playgame.html',{'user':})ur
class playgame(LoginRequiredMixin,ListView):

    template_name = 'ctgctg/playgame.html'
    login_url = '/login/'
    model = models.User
    def get_queryset(self):
        return models.User.objects.all()
class Post(generic.CreateView):
    model=models.Post
    
    fields = ('Image','Title','Description')

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.Username=models.User.objects.filter(username=self.kwargs.get("username")).get()
        self.object.save()
        return super().form_valid(form)


# class playgame2(LoginRequiredMixin,ListView):
#     context_object_name = "lopez"
#     template_name = 'ctgctg/playgame.html'
#     login_url='/login/'
#     model=models.Members
#     def get_queryset(self):
#         return models.Members.objects.all()
def insidepage(request):


    post=models.Post.objects.all()

    return render(request,'ctgctg/insidepage.html',{'post':post})
class Comments_Create(generic.CreateView):
    model=models.post_comments
    fields=['comment']
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.post=models.Post.objects.filter(title_slug=self.kwargs.get("title_slug")).get()
        self.object.user_commented=models.User.objects.filter(username=self.kwargs.get("username")).get()
        self.object.save()
        return super().form_valid(form)
class MusicCreate(generic.CreateView):

    model=models.MusicCreate
    
    template_name = 'ctgctg/music_form.html'
    fields = ['Song_Name','Artist_Name','Song_File','Genre','Cover_Picture','Description']
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user_uploaded=models.User.objects.filter(username=self.kwargs.get("username")).get()
        self.object.save()
        return super().form_valid(form)

class MusicList(generic.ListView):

    model=models.MusicCreate
    template_name = 'ctgctg/music_list.html'
def MusicSearch(request):
    if 'search' in request.GET:
        search_term=request.GET['search']
        music=models.MusicCreate.objects.filter(Song_Name__icontains=search_term)
        return render(request,'ctgctg/music_search.html',{'search_term':search_term,'music':music})
@login_required
def LogoutView(request):

  logout(request)
  return HttpResponse("Logged Out Safetly")

def Dedicate(request):
    return render(request,'ctgctg/dedication.html')
