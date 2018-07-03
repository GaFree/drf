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


# 验证器函数
def about_django(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError("图书不是关于Django的")


class BookInfoSerializer(serializers.Serializer):
    """书籍序列化器"""
    # id 在序列化时使用,read_only 先值字段在序列化是使用
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20, validators=[about_django])
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass

    # 单个字段的校验
    # def validate_btitle(self, value):
    #     # 需求：书名是否包含django字符串
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError('书名不包含django')
    #     # 书名包含django字符串，返回
    #     return value

    # 多字段比较验证
    def validate(self, attrs):
        # attrs 接受前端传来的值
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs

    # 保存验证后的数据
    def create(self, validated_data):
        """增加数据"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.btitle = validated_data('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        # 保存更新的数据到数据库
        instance.sava()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='评论量', max_length=200, required=False, allow_null=True)
    # 外键序列化
    # hbook = serializers.PrimaryKeyRelatedField(label='书籍', read_only=True)
    # hbook = serializers.StringRelatedField(label='书籍')
    # hbook = BookInfoSerializer()
