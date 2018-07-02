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


class BookInfoSerializer(serializers.Serializer):
    """书籍序列化器"""
    # id 在序列化时使用,read_only 先值字段在序列化是使用
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_dqate = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass
