# -*- coding: utf-8 -*-
 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from commodity.models import Commodity
from history.models import History
from user.models import User
from history.models import User_History
from django.forms.models import model_to_dict
from datetime import datetime, timedelta, timezone
import json

def add_commodity(request):
    return render(request, "add_commodity.html")

def commodity(request):
    try:
        query_type = request.GET['type']
        if query_type == 'create':  #先获取商品的信息，包括名字，价格，商品id，版本等等
            name = request.GET['name']
            price = request.GET['price']
            commodity_type = request.GET['commodity_type']
            commodity_id = request.GET['commodity_id']
            edition = request.GET['edition']
            
            if len(Commodity.objects.filter(commodity_id = commodity_id)):  #判断商品是否存在
                return HttpResponse("商品已存在！")
            
            Commodity.objects.create(name = name,
                                 intro = "这是一段简介...",
                                 price = price,
                                 disc_price = price,
                                 commodity_type = commodity_type,
                                 commodity_id = commodity_id,
                                 edition = edition)
            
            return HttpResponse("商品录入成功！")
        elif query_type == 'search_name':
            account = request.GET['account']
            search_text = request.GET['search_text']
            history = History.objects.filter(content=search_text)
            if len(history) == 0:
                History.objects.create(content = search_text,
                                       times = 1)
            else:
                history[0].times += 1
                history[0].save()
            commodity=Commodity.objects.filter(name__contains=search_text)      #类似于SQL的like
            num = len(commodity)
            if num == 0:
                return HttpResponse("找不到商品！")
            data = {}
            L = []
            for i in range(num):
                commodity_info = dict(name=commodity[i].name,           #把商品的信息存成字典形式，方便模板处理
                                commodity_type = commodity[i].get_commodity_type_display(),
                                commodity_id = commodity[i].commodity_id,
                                intro = commodity[i].intro,
                                price = "%.2f" % float(commodity[i].price),
                                disc_price = "%.2f" % float(commodity[i].disc_price),
                                publish_time = commodity[i].publish_time.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"), )  #把日期转化为字符串形式
                L.append(commodity_info)
            data['result'] = L
            data['account'] = account
            #return HttpResponse(json.dumps(data, ensure_ascii=False))
            return render(request, "search_result.html", data)
        elif query_type =='search_type':
            account = request.GET['account']
            commodity_type = request.GET['commodity_type']
            commodity=Commodity.objects.filter(commodity_type = commodity_type)
            num = len(commodity)
            if num == 0:
                return HttpResponse("找不到商品！")
            data = {}
            L = []
            for i in range(num):
                commodity_info = dict(name=commodity[i].name,
                                commodity_type = commodity[i].get_commodity_type_display(),
                                commodity_id = commodity[i].commodity_id,
                                intro = commodity[i].intro,
                                price = "%.2f" % float(commodity[i].price),
                                disc_price = "%.2f" % float(commodity[i].disc_price),
                                publish_time = commodity[i].publish_time.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"), )
                L.append(commodity_info)
            data['result'] = L
            data['account'] = account
            #return HttpResponse(json.dumps(data, ensure_ascii=False))
            return render(request, "search_result.html", data)
        elif query_type == 'view_details':
            account = request.GET['account']
            user = User.objects.filter(account=account)
            commodity_id = request.GET['commodity_id']
            commodity = Commodity.objects.filter(commodity_id=commodity_id)
            commodity_info = dict(name=commodity[0].name,
                                commodity_type = commodity[0].get_commodity_type_display(),
                                commodity_id = commodity[0].commodity_id,
                                intro = commodity[0].intro,
                                price = "%.2f" % float(commodity[0].price),
                                disc_price = "%.2f" % float(commodity[0].disc_price),
                                publish_time = commodity[0].publish_time.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"),
                                edition = commodity[0].edition.split(' '))
            if len(user) > 0:           #表示用户登录了
                user_history = User_History.objects.filter(commodity=commodity[0], user=user[0])
                if len(user_history) == 0:      #用户之前没有浏览过这个商品，创建记录
                    User_History.objects.create(commodity=commodity[0],
                                                user=user[0],
                                                times=1)
                else:       #浏览过，次数加一
                    user_history[0].times += 1
                    user_history[0].save()
                user_history = User_History.objects.filter(user=user[0]).order_by('-times')
                num = len(user_history)
                if num > 5:     #只返回最多5个商品
                    num = 5
                L = []
                for i in range(num):
                    history_info = dict(commodity_id = user_history[i].commodity.commodity_id)
                    L.append(history_info)
                commodity_info['likes'] = L
                commodity_info['account'] = account
            return render(request, "commodity_details.html", commodity_info)
            #return HttpResponse(json.dumps(commodity_info, ensure_ascii=False))
        else:
            return HttpResponse(json.dumps(dict(request_info = 'WRONG TYPE!'), ensure_ascii = False))
    except Exception as e:
        return HttpResponse(json.dumps(dict(request_info = str(e) + '\n' + 'ERROR!'), ensure_ascii = False))
