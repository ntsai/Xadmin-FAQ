# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    #设置文章相关URL
    url(r'^(?P<id>[^/]+)/$','article.views.article',name='article'),
    url(r'^(?P<cid>[^/]+)/(?P<id>[^/]+)/$','article.views.article_show',name='article_show'),
)
