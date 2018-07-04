from django.conf.urls import url
from . import views_old
from rest_framework.routers import DefaultRouter
from . import views
# router = DefaultRouter()  # 实例化对象
# router.register(r'books', views_old.BooksViewSet)  # 在路由器中注册类视图

urlpatterns = [
    # url(r'books/$',views.BooksView)  # 类形式传参
    # 获取全部书籍和增加书籍
    # url(r'^books/$', views.BookInfoView.as_view()),
    # GeneericPAIView
    # url(r'books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
    # # 获取修改删除单个数据
    # url(r'books/(?P<id>\d+)/$', views.BookView.as_view()),
    # 视图集
    url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    url(r'^books/latest/$', views.BookInfoViewSet.as_view({'get': 'latest'})),
    url(r'^books/read/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'post': 'read'})),
]
# urlpatterns += router.urls  # 添加路径
