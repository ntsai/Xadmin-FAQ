#coding:utf-8
#author 'sai'
import xadmin
from xadmin import widgets
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView,ModelAdminView,ListAdminView,CreateAdminView,UpdateAdminView

#列表点击进入Detail
class ListDetailPlugin(BaseAdminPlugin):
    ListDetail = True
    def init_request(self, *args, **kwargs):
        return bool(self.ListDetail)
    def url_for_result(self,__,*args, **kwargs):
        return  self.get_model_url(self.model,'detail',args[0].pk)
xadmin.site.register_plugin(ListDetailPlugin, ListAdminView)

# #新建数据自动保存操作者
# class UserSavePlugin(BaseAdminPlugin):
#     save_uesr = False
#     save_user_model = 'user'
#     def init_request(self, *args, **kwargs):
#         return bool(self.save_uesr)
#
#     def save_models(self,__):
#         __()
#         a = getattr(self.admin_view.new_obj,self.save_user_model)
#         a = self.user
#         a.save()
#
# xadmin.site.register_plugin(UserSavePlugin, CreateAdminView)