from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # 实例化对象
router.register(r'books', views.BooksViewSet)  # 在路由器中注册类视图

urlpatterns = [
    # url(r'books/$',views.BooksView)  # 类形式传参
    # 获取全部书籍和增加书籍
    # url(r'^books/$', views.BooksView.as_view()),
    # # 获取修改删除单个数据
    # url(r'books/(?P<id>\d+)/$', views.BookView.as_view()),
]
urlpatterns += router.urls  # 添加路径