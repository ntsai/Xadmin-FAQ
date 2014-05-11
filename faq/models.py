#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Faq(models.Model):
    title = models.CharField(u"标题", max_length=200)
    num = models.FloatField(u'序号',max_length=2,unique=False)
    content = models.TextField(u"内容",null=True, blank=True)
    parent = models.ForeignKey('self',null=True, blank=True,verbose_name=u'问题类别')
    author = models.ForeignKey(User,verbose_name=u"作者",blank=True,null=True)
    time = models.DateTimeField(u"创建时间",auto_now=True)

    class Meta:
        verbose_name=u'问题'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.num) + ' ' + self.title