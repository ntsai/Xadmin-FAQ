#coding:utf-8
import xadmin
from xadmin.layout import Fieldset, Field,Row
from models import *

class FaqAdmin(object):
    def name(self,instance):
        if instance.parent:
            n = '&nbsp;'*6 + instance.title
            return '<a href="%s">%s</a>' % (self.get_model_url(Faq,'detail',instance.pk),n)
        if self.user.is_superuser:
            return '<a href="%s">%s</a>' % (self.get_model_url(Faq,'detail',instance.pk),instance.title)
        return instance.title
    name.short_description = '&nbsp;'
    name.allow_tags = True
    name.allow_export = False
    name.is_column = False

    use_related_menu = False
    actions = None
    list_export = ()
    object_list_template = 'faq_model_list.html'
    # exclude = ('author',)
    list_display = ('name',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title','parent',)
    relfield_style = 'fk-ajax'
    form_layout = (
        Fieldset('基本信息',
            Row('title','parent'),
            Row('num','author'),
        ),
        Fieldset('内容',
            'content'
        )
    )
    style_fields = {'content': 'ueditor',}

    def get_list_queryset(self):
        qs = super(FaqAdmin,self).get_list_queryset().order_by('num')
        if self.request.is_ajax():
           return qs.filter(parent__isnull = True)
        return qs

xadmin.site.register(Faq,FaqAdmin)

