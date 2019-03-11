from django.http import HttpResponse
import json

import os.path


def defaultRet(data):
    return responseData(0, data, '')


def responseData(code, data, msg):
    ret = {'code':code, 'data':data, 'msg':msg}
    return ret



# def readHerolist():
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     file_path = BASE_DIR + '/templates/hero_list.json'
#     # file = open('./wzry/templates/hero_list.json', 'r', encoding='utf-8')
#     file = open(file_path, 'r', encoding='utf-8')
#
#     ret = json.load(file)
#     file.close()
#     return ret


def readHerolist():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = BASE_DIR + '/templates/hero_list.json'
    # file = open('./wzry/templates/hero_list.json', 'r', encoding='utf-8')
    file = open(file_path, 'r', encoding='utf-8')
    allArray = json.load(file)
    file.close()

    ret = []
    for obj in allArray:
        tech = {'ename', 'cname', 'type'}
        techDict = {key: value for key, value in obj.items() if key in tech}
        ret.append(techDict)

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