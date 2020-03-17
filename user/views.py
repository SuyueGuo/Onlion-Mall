# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from user.models import User
import json

# 表单
def register_form(request):
    return render(request, 'register_form.html')

def login_form(request):
    return render(request, 'login_form.html')
 
# 接收请求数据
def get_user_info(user):
    return json.dumps(dict(address = user.address,
                           telephone = str(user.telephone),
                           head_portrait = user.head_portrait, ))
@csrf_exempt
def user(request):
    try:
        if request.method == 'GET':
            query_type = request.GET['type']
        else:
            query_type = request.POST['type']
        if query_type == 'create':  #创建用户
            name = request.POST['name'] #得到姓名，账号，密码，地址，电话等信息
            account = request.POST['account']
            password = request.POST['password']
            address = request.POST['address']
            telephone = int(request.POST['telephone'])
            
            arr = User.objects.filter(account=account)
            if len(arr) == 0:       #账号不存在，创建成功
                User.objects.create(name = name, account = account, password = password, address = address, telephone = telephone)
                return HttpResponse("注册成功!")
            else:
                return HttpResponse("该账号已存在!")
            
        elif query_type == 'login':
            account = request.POST['account']
            password = request.POST['password']
            arr = User.objects.filter(account=account)
            if len(arr) == 0:   
                return HttpResponse("不存在的账号!")
            else:
                if arr[0].password == password:
                    data = {}
                    data['is_login'] = '1'
                    data['account'] = arr[0].account
                    data['name'] = arr[0].name
                    return render(request, 'index.html', data)
                    #return HttpResponse("账号密码正确!")
                else:
                    return HttpResponse("账号或密码错误!")
            
        elif query_type == 'modify':
            name = request.GET['name']
            address = request.GET['address']
            telephone = int(request.GET['telephone'])
            head_portrait = request.GET['head_portrait']
            
            arr = User.objects.filter(name = name)
            if len(arr) == 1:
                arr[0].address = address
                arr[0].telephone = telephone
                arr[0].head_portrait = head_portrait
                arr[0].save()
                return HttpResponse(json.dumps(dict(request_info = 'UPDATED!'), ensure_ascii = False))
            else:
                return HttpResponse(json.dumps(dict(request_info = 'ERROR!'), ensure_ascii = False))
            
            
        else:
            return HttpResponse(json.dumps(dict(request_info = 'WRONG TYPE!'), ensure_ascii = False))
        
    except Exception as e:
        return HttpResponse(json.dumps(dict(request_info = str(e) + '\n' + 'ERROR!'), ensure_ascii = False))
					
def home_page(request):
    data = {}
    data['is_login'] = '0'
    return render(request, 'index.html', data)

def page_not_found(request, exception):
    return render(request, '404.html')
    
