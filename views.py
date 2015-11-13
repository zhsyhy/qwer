q# -*- coding: utf-8 -*-
from django.template import RequestContext 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from addr.models import User
from addr.models import order
def main_page(request):
    output = '''
    <html align='center' >
    <head><title>%s</title></head>
    <body  background="/site_media/02.gif"  >
    <h1>%s</h1><p>%s</p>
    <p>
    <a href='http://127.0.0.1:8000/registe/'>注册</a>
    <a href='http://127.0.0.1:8000/login/'>登录</a></p>
    <img src="/site_media/4.jpg" width=900>
    </body>
    </html>
    ''' % (
    '教师信息管理',
    '欢迎使用教师信息管理软件',
    '欢迎使用',
    )
    return HttpResponse(output)
def registe(request):
    if request.POST:
        post = request.POST
        new_people = User(
        Username = post["Username"],
        Password = post["Password"],
        Leixing  = post["L"],
        )
        new_people.save()
        user_list = User.objects.all()
        return render_to_response("registe1.html",{'author_list':user_list,},context_instance=RequestContext(request))
    user_list = User.objects.all()
    return render_to_response("registe.html",{'author_list':user_list,},context_instance=RequestContext(request))
def login(request):
    
    if request.POST:
        post = request.POST
        for user in User.objects.all():
            if user.Username == post["Username"] and user.Password == post["Password"]:
                if user.Leixing == "student"  and post["L"] == "student":

                    return render_to_response("student.html",{'user':user}, context_instance=RequestContext(request))
                    
                elif user.Leixing == "teacher" and post["L"] == "teacher":
                    return render_to_response("teacher.html",{'user':user,},context_instance=RequestContext(request))
        return render_to_response("loginfalse.html", context_instance=RequestContext(request))
    return render_to_response("login.html", context_instance=RequestContext(request))
def teacher(request):
    n = request.GET['id']
    if request.POST:
        for user in User.objects.all():
           if n == user.Username:
                post = request.POST
                user.Name = post["Name"]
                user.Email = post["Email"]
                user.Phone  = post["Phone"]
                user.Labroom  = post["Labroom"]
                user.Workroom  = post["Workroom"]
                user.Achievement  = post["Achievement"]
                user.Date  = post["Date"]
                user.Study  = post["Study"]
                user.save()
                return render_to_response("form.html",{'user_list':user,} ,context_instance=RequestContext(request))
    for user in User.objects.all():
        if n == user.Username:
            return render_to_response("form2.html",{'user_list':user,} ,context_instance=RequestContext(request))
def search(request):
    studentuser = request.GET['id']
    for use in User.objects.all():
        if use.Username == studentuser:
            user1 = use
    if request.POST:
        post = request.POST
        for user in User.objects.all():
            if post["search"] == user.Name:
                return render_to_response("show1.html",{'user':user,'user1':user1,} ,context_instance=RequestContext(request))
    
    return render_to_response("check.html", context_instance=RequestContext(request))
def recommend(request):
    if request.POST:
        post = request.POST
        for user in User.objects.all():
            if user.Study == post["search"]:
                user_list = User.objects.filter(Study = post["search"])
                return render_to_response("tuijian.html",{'user_list':user_list,},context_instance=RequestContext(request))
        return render_to_response("nosearch.html",context_instance=RequestContext(request))
    return render_to_response("recommend.html",context_instance=RequestContext(request))
def order1(request):
    username = request.GET['id']
    name = request.GET['classid']
    for use in User.objects.all():
        if use.Username == username:
            user1 = use  
    for a in User.objects.all():
        if a.Name == name:
            user = a
    if request.POST:
        post = request.POST
        new_order = order(              
        orderusername = post["orderusername"],
        daoshi = post["daoshi"],
        xingming  = post["xingming"],
        orderdata  = post["orderdata"],
        telephone  = post["telephone"],)
        new_order.save()
        return render_to_response("ordersuccess.html",{'order':new_order,},context_instance=RequestContext(request))
    return render_to_response("order1.html",{'user':user1,'user1':user,},context_instance=RequestContext(request))
def jiancha(request):
    n = request.GET['id']
    for neworder in order.objects.all():
        if n == neworder.daoshi:
            order_list = order.objects.filter(daoshi = n)
            return render_to_response("jiancha.html",{'orderlist':order_list,},context_instance=RequestContext(request))
    return render_to_response("jianchareturn.html",context_instance=RequestContext(request))

