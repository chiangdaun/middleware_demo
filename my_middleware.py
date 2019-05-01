# -*- coding:utf-8 -*-
"""
Author:duan
Date:2019/4/30 13:32
"""
from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# 定义一个可以访问的白名单
URL = ["/oo/", "/xx/", "/haha/"]


class MD1(MiddlewareMixin):

    def process_request(self, request):
        print("MD1里面的 process_request")
        # print(id(request))

        # print(request.path_info)  # /index/
        # print(request.get_full_path())  # /index/?name=xiaohei&age=23

        # 如果用户请求的url在白名单里,则什么都不做,继续执行请求
        # if request.path_info in URL:
        #     return
        # # 否则直接返回响应,不再往后执行
        # else:
        #     return HttpResponse('gun!')

    def process_response(self, request, response):
        print("MD1里面的 process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        :param request: 浏览器发来的请求对象
        :param view_func: 将要执行的视图函数的名字
        :param view_args: 将要执行的视图函数的位置参数
        :param view_kwargs: 将要执行的视图函数的关键字参数
        :return:
        """

        print("-" * 80)
        print("MD1 中的process_view")
        print(view_func, view_func.__name__)


class MD2(MiddlewareMixin):
    def process_request(self, request):
        # print(id(request))
        print("MD2里面的 process_request")

    def process_response(self, request, response):
        print("MD2里面的 process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("-" * 80)
        print("MD2 中的process_view")
        print(view_func, view_func.__name__)
