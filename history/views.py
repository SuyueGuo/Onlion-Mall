# -*- coding: utf-8 -*-
 
from django.http import HttpResponse, JsonResponse
from history.models import History
from django.forms.models import model_to_dict
import json

def history(request):
    try:
        query_type = request.GET['type']
        if query_type == 'get_history':
            search_text = request.GET['search_text']
            historys = History.objects.filter(content__contains=search_text).order_by('-times') #按次数降序排列
            data = ''
            num = len(historys)
            for i in range(num):
                data = data + historys[i].content + ' '
            return HttpResponse(data)
        else:
            return HttpResponse(json.dumps(dict(request_info = 'WRONG TYPE!'), ensure_ascii = False))
    except Exception as e:
        return HttpResponse(json.dumps(dict(request_info = str(e) + '\n' + 'ERROR!'), ensure_ascii = False))
