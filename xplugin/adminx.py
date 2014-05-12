#coding:utf-8
import xadmin

class GolbeSetting(object):
    # menu_style = 'accordion'
    site_title = u'Xadmin FAQ'
    base_template = 'faq_base_site.html'
xadmin.site.register(xadmin.views.CommAdminView, GolbeSetting)