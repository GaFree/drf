from django.db import models


# Create your models here.

class BookInfo(models.Model):
    """定义模型类"""
    btitle = models.CharField(max_length=20, verbose_name="书籍名字")
    bpub_date = models.DateField(verbose_name="发布日前")
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    image = models.ImageField(upload_to='img',verbose_name='封面',null= True)  # 传图片  upload_to='img'是 static_files/media 路径下的创建图片
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名 # TODO 更改数据库表名
        verbose_name = '武侠小说'  # admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的是复数名称

    # py3 的写法
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')
    pub_date.short_description = '发布日期'  # 设置方法字段在admin中显示的标题
    pub_date.admin_order_field = 'bpub_date'
