# -*- coding: utf-8 -*-
 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from commodity.models import Commodity
from user.models import User
from trade.models import Trade
from comment.models import Comment
from django.forms.models import model_to_dict
from datetime import datetime, timedelta, timezone
from django.db.models import Q

import json


def comment(request):
    try:
        query_type = request.GET['type']
        if query_type == 'create':
            account = request.GET['account']
            commodity_id = request.GET['commodity_id']
            content = request.GET['content']
            score = request.GET['score']
            trade_id = request.GET['trade_id']
            
            commodity = Commodity.objects.get(commodity_id = commodity_id)
            user = User.objects.get(account = account)

            Comment.objects.create(commodity = commodity,
                                    user = user,
                                    content = content,
                                    score = int(score),
                                    trade_id = trade_id)
            trade = Trade.objects.get(trade_id = trade_id)
            trade.state = '4'
            trade.save()
            return HttpResponse("评论成功！")
        elif query_type == 'make_comment':
            trade_id = request.GET['trade_id']

            trade = Trade.objects.get(trade_id = trade_id)
            data = {}
            data['commodity_name'] = trade.commodity.name
            data['edition'] = trade.edition
            data['total_price'] = trade.total_price
            data['commodity_id'] = trade.commodity.commodity_id
            data['edition_id'] = trade.edition_id
            data['trade_id'] = trade.trade_id
            return render(request, "make_comment.html", data)
        elif query_type == 'view_comments':
            account = request.GET['account']

            user = User.objects.get(account = account)
            comment = Comment.objects.filter(user = user)
            data = {}
            num = len(comment)
            L = []
            for i in range(num):
                trade = Trade.objects.filter(trade_id = comment[i].trade_id)
                tmp = dict(commodity_name = comment[i].commodity.name,
                           commodity_id = comment[i].commodity.commodity_id,
                           content = comment[i].content,
                           score = comment[i].score,
                           create_time = comment[i].create_time.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"),
                           edition = trade[0].edition,
                           edition_id = trade[0].edition_id)
                L.append(tmp)
            data['comments'] = L
            data['account'] = account
            return render(request, "check_comment.html", data)
        
        else:
            return HttpResponse(json.dumps(dict(request_info = 'WRONG TYPE!'), ensure_ascii = False))
    except Exception as e:
        return HttpResponse(json.dumps(dict(request_info = str(e) + '\n' + 'ERROR!'), ensure_ascii = False))
