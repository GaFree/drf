from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View


# Create your views here.

# 获取全部的书籍
# get/books

# 增加书籍
# post/books

class BooksView(View):
    def get(self, request):
        """获取全部的书籍"""
        pass

    def post(self, request):
        """增加书籍"""
        pass

# 获取一本书籍
# get/books/id
# books/(?P<id>\d+)/$
# 删除书籍
# delete/books/id
# 修改一本书
# put/books/id