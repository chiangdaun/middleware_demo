from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print("这是app01的index视图函数")
    return HttpResponse('o98k')
