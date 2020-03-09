from django.db import models
from datetime import datetime
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField('姓名',max_length=20)
    mobile = models.CharField('手机',max_length=11)
    course_name = models.CharField('课程名',max_length=50)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name