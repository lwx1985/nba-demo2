# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from userControl import models
from django import forms
from django.forms import widgets
from django.forms import fields


def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # obj = models.UserInfo.objects.filter(username=u,password=p).first()
        # print(obj)# obj None,
        # count = models.UserInfo.objects.filter(username=u, password=p).count()
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            res = redirect('/userControl/index/')
            res.set_signed_cookie('user_nba_data', u, max_age=10, salt='nba-data')
            # res.set_cookie('user_nba_data', u, max_age=10)
            return res
        else:
            return HttpResponse("username or password error")
    else:
        # PUT,DELETE,HEAD,OPTION...
        return redirect('/userControl/index/')


def auth(func):
    def inner(reqeust ,*args,**kwargs):
        # v = reqeust.COOKIES.get('user_nba_data')
        v = reqeust.get_signed_cookie('user_nba_data', salt='nba-data')
        if not v:
            return redirect('/userControl/login/')
        return func(reqeust, *args,**kwargs)
    return inner


@auth
def index(reqeust):
    # 获取当前已经登录的用户
    # u = reqeust.COOKIES.get('user_nba_data')
    u = reqeust.get_signed_cookie('user_nba_data', salt='nba-data')
    user_list = models.UserInfo.objects.all()
    return render(reqeust, 'index.html', {'current_user': u, 'user_list': user_list})

# def index(request):
#     user_list = models.UserInfo.objects.all()
#     # print(user_list.query)
#     # QuerySet [obj,obj,]
#     return render(request, 'index.html', {'user_list': user_list})


def orm(request):
    dic = { 'player__icontains' : 'paul','ps_g__gte' : '10.0'}

    result = models.Season2017.objects.filter(**dic)
    # print(len(result))
    # models.UserInfo.objects.create(username='a',password='1985')
    for row in result:
        print(row.player)
    return HttpResponse("ok")


class FM(forms.Form):
    # 字段本身只做验证
    username = fields.CharField(
        max_length=12,
        min_length=6,
        )
    password = fields.CharField(
        max_length=12,
        min_length=6,
    )
    # email = fields.EmailField(error_messages={'required': '邮箱不能为空.','invalid':"邮箱格式错误"})


def sign(request):
    if request.method == "GET":
        return render(request, 'sign.html')
    elif request.method == 'POST':
        # u = request.POST.get('username')
        # p = request.POST.get('password')
        # models.UserInfo.objects.create(username=u,password=p)
        user_data = FM(request.POST)
        judge = user_data.is_valid()
        if judge:
            models.UserInfo.objects.create(**user_data.cleaned_data)
        else:
            print(user_data.errors.as_json())
            return render(request, 'sign.html')
        return HttpResponse("ok")
    else:
        return render(request, 'sign.html')









