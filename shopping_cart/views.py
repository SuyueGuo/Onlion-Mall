# -*- coding: utf-8 -*-
 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from commodity.models import Commodity
from user.models import User
from shopping_cart.models import Shopping_Cart
from django.forms.models import model_to_dict
from datetime import datetime, timedelta, timezone
from django.db.models import Q

import json


def shopping_cart(request):
    try:
        query_type = request.GET['type']
        if query_type == 'create':
            account = request.GET['account']
            commodity_id = request.GET['commodity_id']
            edition = request.GET['edition']
            edition_id = request.GET['edition_id']
            
            commodity = Commodity.objects.get(commodity_id = commodity_id)
            user = User.objects.get(account = account)

            order = Shopping_Cart.objects.filter(user = user, commodity = commodity, edition_id = edition_id)
            if(len(order) == 0):        #商品不在购物车里，数目为1
                Shopping_Cart.objects.create(commodity = commodity,
                                         user = user,
                                         number = 1,
                                         edition = edition,
                                         edition_id = edition_id,)

            else:               #商品在购物车里，数目加一
                order[0].number += 1
                order[0].save()
            return HttpResponse("成功加入购物车！")
        elif query_type == 'view':
            account = request.GET['account']
            user = User.objects.get(account = account)
            order = Shopping_Cart.objects.filter(user = user)
            data = {}
            tmp = []
            num = len(order)
            if num == 0:
                return render(request, "shopping_cart.html", data)
            for i in range(num):
                order_info = dict(name = order[i].commodity.name,
                                  commodity_id = order[i].commodity.commodity_id,
                                  edition = order[i].edition,
                                  number =  order[i].number,
                                  edition_id = order[i].edition_id,
                                  price = order[i].commodity.price,
                                  disc_price = order[i].commodity.disc_price,
                                  total_price = str(float(order[i].commodity.price) * int(order[i].number)),)
                tmp.append(order_info)
            data['result'] = tmp
            data['account'] = account
            return render(request, "shopping_cart.html", data)
        elif query_type == 'delete':
            account = request.GET['account']
            commodity_id = request.GET['commodity_id']
            edition_id = request.GET['edition_id']
            
            commodity = Commodity.objects.get(commodity_id = commodity_id)
            user = User.objects.get(account = account)

            Shopping_Cart.objects.get(commodity = commodity, user = user,edition_id = edition_id).delete()
            
            return HttpResponse("删除成功！")
        else:
            return HttpResponse(json.dumps(dict(request_info = 'WRONG TYPE!'), ensure_ascii = False))
    except Exception as e:
        return HttpResponse(json.dumps(dict(request_info = str(e) + '\n' + 'ERROR!'), ensure_ascii = False))
