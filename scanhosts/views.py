from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from scanhosts.models import *
import json


def user_info(request):
    ip_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']

    user_obj = UserIPInfo.objects.filter(ip=ip_addr)

    if not user_obj:
        res = UserIPInfo.objects.create(ip=ip_addr)
        ip_addr_id = res.id
    else:
        ip_addr_id = user_obj[0].id

    BrowseInfo.objects.create(useragent=user_ua, userIp_id=ip_addr_id)

    # result = {
    #     "STATUS": "SUCCESS",
    #     "INFO": "USER INFO",
    #     "IP": ip_addr,
    #     "UA": user_ua
    # }
    result = "STATUS : SUCCESS \n INFO   : USER INFO \n IP     : %s \n UA     : %s \n " % (ip_addr, user_ua)

    # return HttpResponse(json.dumps(result), content_type='application/json')
    return HttpResponse(result)


def user_history(request):
    ip_list = UserIPInfo.objects.all()
    print(ip_list)
    infos = {}
    for item in ip_list:
        infos[item.ip] = [b_obj.useragent for b_obj in BrowseInfo.objects.filter(userIp_id=item.id)]

    result = "STATUS : SUCCESS" \
             "INFO: %s" % infos

    return HttpResponse(result)
