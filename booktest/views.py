from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.views.generic import View
import json

# Create your views here.

# 获取全部的书籍
# get/books

# 增加书籍
# post/books
from booktest.models import BookInfo


class BooksView(View):
    def get(self, request):
        """获取全部书籍"""
        # 获取全部书籍
        books = BookInfo.objects.all()
        '''
        [

            {'btitle': '西游记', 'bpub_date': '1986-12-12', ....}
            .......

        ]


        '''
        # 数据格式转化
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            })

        # 展示书籍
        # JsonResponse默认只接受字典，
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """增加书籍"""
        # 获取前端传来的数据
        body_data = request.body
        # 转码
        str_data = body_data.decode()
        data = json.loads(str_data)

        # TODO 数据进行校验

        # 写入数据库
        book = BookInfo.objects.create(
            btitle=data['btitle'],
            bpub_date=data['bpub_date']
        )
        # 展示数据
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })


class BookView(View):
    def get(self, request, id):
        '''获取一本书籍'''
        # 查询数据库，要判断是否存在
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            raise e
        # 展示数据返回

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def put(self, request, id):
        '''修改一本书'''
        # 查询数据库，要判断是否存在
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            raise e

        # 获取前端传来的数据
        body_data = request.body
        # 转码
        str_data = body_data.decode()
        data = json.loads(str_data)

        # 修改数据
        book.btitle = data['btitle']
        book.bpub_date = data['bpub_date']
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def delete(self, request, id):
        # 删除书籍
        # 查询数据库，要判断是否存在
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            raise e
        book.delete()
        return HttpResponse
