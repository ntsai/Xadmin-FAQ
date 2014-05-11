#coding:utf-8
from  django.shortcuts  import  render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.template.loader import get_template
from article.models import *
from ad.models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from userena.models import UserenaBaseProfile
from lbforum.models import Topic
from book.views import pagelist
from order.models import Cart

#文章列表
def article(request,id):
    nav = Nav.objects.all().order_by("order")  #栏目
    last_nav = Nav.objects.all().order_by("-order")[0]  #网站说明
    try:
        cart_count = Cart.objects.get(user=request.user).product.all() #购物车
    except:
        pass

    name = Category.objects.get(id=id)
    article = sorted(Article.objects.filter(categories=name).order_by("-time"), key=lambda np: np.istop(id),reverse=True)

    try:
        if request.GET["time"] == '1':
            article = Article.objects.filter(categories=name).order_by('-time') #当前页面文章列表
            time_bottom = True

        elif request.GET["time"] == '2':
            article = Article.objects.filter(categories=name).order_by('time') #当前页面文章列表
            time_top = True
    except:
        time_top = True

    try:
        if request.GET["title"] == '1':
            article = Article.objects.filter(categories=name).order_by('-title') #当前页面文章列表
            title_bottom = True

        elif request.GET["title"] == '2':
            article = Article.objects.filter(categories=name).order_by('title') #当前页面文章列表
            title_top = True
    except:
        title_top = True


    cid = int(Category.objects.all().order_by('-id')[0].id)
    cat = Category.objects.all()
    ex_cat = Category.objects.exclude(id=id)
    bbs = Topic.objects.filter(sticky=True)

    if cid == int(id):
        #top 右侧头部文章
        top_new = sorted(Article.objects.filter(categories__id = cat[0].id).order_by("-time"), key=lambda np: np.istop(cat[0].id),reverse=True)#右侧文章列表
        top = cat[0] #右侧文章标题
        #mid 右侧中部文件
        mid_new = sorted(Article.objects.filter(categories__id = cat[1].id).order_by("-time"), key=lambda np: np.istop(cat[1].id),reverse=True)#右侧文章列表
        mid = cat[1] #右侧文章标题
    else:
        #top 右侧头部文章
        top_new = sorted(Article.objects.filter(categories__id = ex_cat[0].id).order_by("-time"), key=lambda np: np.istop(ex_cat[0].id),reverse=True)#右侧文章列表
        top = ex_cat[0] #右侧文章标题
        #mid 右侧中部文件
        mid_new = sorted(Article.objects.filter(categories__id = ex_cat[1].id).order_by("-time"), key=lambda np: np.istop(ex_cat[1].id),reverse=True)#右侧文章列表
        mid = ex_cat[1]#右侧文章标题

    list = pagelist(request,article)
    paginator = list["paginator"]
    page = list["page"]
    first = list["first"]
    second = list["second"]
    last_second = list["last_second"]
    last = list["last"]
    data = list["data"]
    t = get_template('article/article.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

#文章详细
def article_show(request,cid,id):
    nav = Nav.objects.all().order_by("order")  #栏目
    last_nav = Nav.objects.all().order_by("-order")[0]  #网站说明
    try:
        cart_count = Cart.objects.get(user=request.user).product.all() #购物车
    except:
        pass


    name = Category.objects.get(id=cid)
    article = Article.objects.get(id=id)                                                                            #当前文章
    bbs = Topic.objects.filter(sticky=True)
    ex_cat = Category.objects.exclude(id=cid)

    top_title = ex_cat[0]                                                                #右侧头部文章栏目
    top = sorted(Article.objects.filter(categories__id = ex_cat[0].id).order_by("-time"), key=lambda np: np.istop(ex_cat[0].id),reverse=True)

    mid_title = ex_cat[1]                                                                 #右侧中部文章栏目
    mid = sorted(Article.objects.filter(categories__id = ex_cat[1].id).order_by("-time"), key=lambda np: np.istop(ex_cat[1].id),reverse=True)

    t = get_template('article/article_show.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

