from rest_framework import serializers
from .models import BookInfo


class BookInfoSerializers(serializers.ModelSerializer):
    """书籍模型类序列化器"""

    class Meta:
        # 要系列化或者反序列化的模型类
        model = BookInfo
        # 把所有的字段都显示
        # fields = ['id','btitle'] 展示指定字段
        fields = '__all__'
