from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookInfo
from .serializers import BookInfoSerializer
from rest_framework.generics import GenericAPIView
import json
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ViewSetMixin, ViewSet,ModelViewSet


# 获取全部书籍，运行序列化并返回
# class BookInfoView(ListModelMixin, GenericAPIView, CreateModelMixin):
# class BookInfoView(ListAPIView,CreateAPIView):
class BookInfoView(ListCreateAPIView):
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    # def get(self, request):
    #     """
    #     :param request: DRf 的Request的对象
    #     :return:
    #     """
    #     # # 1. 数据库查询
    #     # books = BookInfo.objects.all()
    #     # # 2. 格式转化
    #     # ser = BookInfoSerializer(books, many=True)
    #     # # 3. 返回
    #     # return Response(ser.data)
    #     return self.list(request)
    #
    # def post(self, request):
    #     # 获取前端来的数据
    #     # body_data = request.data
    #     # str_data = body_data.decode()
    #     # data = json.loads(str_data)
    #     # request 是DRF封装好的类字典
    #
    #     # ser = BookInfoSerializer(data=request.data)
    #     # # 校验数据
    #     # ser.is_valid(raise_exception=True)
    #     # # 写入数据库
    #     # ser.save()
    #     # 写入数据库
    #     # 返回
    #     # return Response(ser.data)
    #     return self.create(request)


# 获取一本书

class BookDetailView(GenericAPIView, RetrieveModelMixin):
    serializer_class = BookInfoSerializer
    # 查询集
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        # 查询数据判断是否存在
        # try:
        #     book = BookInfo.objects.get(id=pk)
        # except BookInfo.DoesNotExist:
        #     return Response('数据不存在')
        #
        # book = self.get_object()
        # # 序列化
        # ser = BookInfoSerializer(book)
        # return Response(ser.data)
        return self.retrieve(request)


# class BookInfoViewSet(ViewSet):
# class BookInfoViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin):
class BookInfoViewSet(ModelViewSet):
    """视图集使用"""
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()
    # def list(self, request):
    #     book = BookInfo.objects.all()
    #     ser = BookInfoSerializer(book, many=True)
    #     return Response(ser.data)
    #
    # def retrieve(self, request, pk):
    #     try:
    #         book = BookInfo.objects.get(id=pk)
    #     except BookInfo.DoesNotExist:
    #         return Response("数据不存在！！")
    #
    #     ser = BookInfoSerializer(book)
    #     return Response(ser.data)
    @action(methods=['get'], detail=False)
    def latest(self, request):
        """获取最新的书"""
        # 查询数据库
        # latest()获取最新的数据对象
        book = BookInfo.objects.latest('id')
        # 序列化
        ser = self.get_serializer(book)
        # 返回
        return Response(ser.data)

    def read(self, request,pk):
        """更新书籍"""
        # 查询数据库
        book = self.get_object()
        # 校验
        # 更新数据库
        ser = self.get_serializer(book, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        # 返回
        return Response(ser.data)
