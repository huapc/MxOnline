from django.db import models
from datetime import datetime
# Create your models here.

class CourseOrg(models.Model):
    name = models.CharField('机构名称', max_length=50)
    desc = models.TextField('机构描述')
    click_nums = models.IntegerField('点击数', default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    image = models.ImageField('封面图', upload_to='org/%Y%m', max_length=100)
    address = models.CharField('机构地址', max_length=150)
    city = models.ForeignKey(CityDict, verbose_name='所在城市', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name