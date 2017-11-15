#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from login.models import User
import pdb
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

def regist(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            userResult=User(username=username,password=password,email=email)
            userResult.save()

            #return HttpResponse('regist success!!!')
            return render(request,'login/jumpToIndex.html')
    else:
        userform = UserForm()
    return render(request,'login/regist.html',{'userform':userform})

def login(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username__exact=username,password__exact=password)
            # user = authenticate(username=username,password=password)
            if user:
                return HttpResponseRedirect(reverse('polls:index'))
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render(request,'login/login.html',{'userform':userform})

def index(request):
    return render(request,'login/loginIndex.html')

