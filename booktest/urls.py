from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'books/$',views.BooksView)  # 类形式传参
    # 获取全部书籍和增加书籍
    url(r'^books/$', views.BooksView.as_view()),
    # 获取修改删除单个数据
    url(r'books/(?P<id>\d+)/$', views.BookView.as_view()),
]
