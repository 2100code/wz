from django.http import HttpResponse
import json


def defaultRet(data):
    return responseData(0, data, '')


def responseData(code, data, msg):
    ret = {'code':code, 'data':data, 'msg':msg}
    return ret



def readHerolist():
    file = open('./wzry/templates/hero_list.json', 'r', encoding='utf-8')
    ret = json.load(file)
    file.close()
    return ret

def index(request):
    return HttpResponse("wz 数据更新3")

def herolist(request):
    ret = readHerolist();
    ret = defaultRet(ret)
    return HttpResponse(json.dumps(ret))


def hero(request, nameNum):
    array = readHerolist();
    ret = {}
    for heroObject in array:
        num = heroObject['ename']
        if str(num) == nameNum :
            ret = heroObject
    ret = defaultRet(ret)
    return HttpResponse(json.dumps(ret))