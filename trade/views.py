# -*- coding: utf-8 -*-
 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from commodity.models import Commodity
from user.models import User
from trade.models import Trade
from django.forms.models import model_to_dict
from datetime import datetime, timedelta, timezone
from django.db.models import Q

import json


def trade(request):
    try:
        query_type = request.GET['type']
        if query_type == 'create':#这个是在购物车里生成订单
            account = request.GET['account']
            commodity_id = request.GET['commodity_id']
            edition = request.GET['edition']
            edition_id = request.GET['edition_id']
            trade_id = request.GET['trade_id']
            number = request.GET['number']
            total_price = request.GET['total_price']
            
            commodity = Commodity.objects.get(commodity_id = commodity_id)
            user = User.objects.get(account = account)

            Trade.objects.create(commodity = commodity,
                                         user = user,
                                         number = int(number),
                                         edition = edition,
                                         edition_id = edition_id,
                                         trade_id = trade_id,
                                         total_price = float(total_price))
            
            return HttpResponse("购买成功!")
        elif query_type == 'create_2':#这个是在商品界面生成订单
            account = request.GET['account']
            commodity_id = request.GET['commodity_id']
            edition = request.GET['edition']
            edition_id = request.GET['edition_id']
            trade_id = request.GET['trade_id']
            number = request.GET['number']
            
            commodity = Commodity.objects.get(commodity_id = commodity_id)
            user = User.objects.get(account = account)

            Trade.objects.create(commodity = commodity,
                                         user = user,
                                         number = int(number),
                                         edition = edition,
                                         edition_id = edition_id,
                                         trade_id = trade_id,
                                         total_price = commodity.price)
            
            return HttpResponse("成功购买"+ commodity.name + ' ' + edition + '!')
        elif query_type == 'view':
            account = request.GET['account']
            user = User.objects.get(account = account)

            trades = Trade.objects.filter(user = user)
            num = len(trades)
            data = {}
            if num == 0:
                return render(request, "user_order.html", data)
            L = []
            for i in range(num):
                trade_info = dict(commodity_name = trades[i].commodity.name,
                                commodity_id = trades[i].commodity.commodity_id,
                                number = str(trades[i].number),
                                trade_id = trades[i].trade_id,
                                state = trades[i].state,
                                price = "%.2f" % float(trades[i].commodity.price),
                                disc_price = "%.2f" % float(trades[i].commodity.price),
                                time = trades[i].time.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"),
                                commodity_edition = trades[i].edition,
                                edition_id = trades[i].edition_id,
                                total_price = trades[i].total_price)
                L.append(trade_info)
            data['result'] = L
            data['account'] = account
            #return HttpResponse(json.dumps(data, ensure_ascii=False))
            return render(request, "user_order.html", data)
        elif query_type == 'change_state':
            trade_id = request.GET['trade_id']
            new_state = request.GET['new_state']

            order = Trade.objects.get(trade_id = trade_id)
            order.state = new_state
            order.save()

            return HttpResponse("状态修改成功！")
        elif query_type == 'delete':
            trade_id = request.GET['trade_id']

            Trade.objects.get(trade_id = trade_id).delete()

            return HttpResponse("删除成功！")
        
        else:
            return HttpResponse(json.dumps(dict(request_info = 'WRONG TYPE!'), ensure_ascii = False))
    except Exception as e:
        return HttpResponse(json.dumps(dict(request_info = str(e) + '\n' + 'ERROR!'), ensure_ascii = False))
