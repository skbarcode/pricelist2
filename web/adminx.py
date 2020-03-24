# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from xadmin import views
from web.models import Supplier, Goods, Brand
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class GlobalSittings(object):
    # global_search_models = ['Gmodel']
    site_title = '斯康后台管理系统'
    site_footer = '斯康在线网'
    menu_style = 'accordion'


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GoodsResources(resources.ModelResource):
    class Meta:
        model = Goods



class GoodsAdmin(object):
    import_export_args = {'import_resource_class': GoodsResources, 'export_resource_class': GoodsResources}

    list_display = (
        'brand', 'Gmodel', 'unit', 'type', 'price', 'min_price', 'meno', 'supplier', 'date',)
    search_fields = ('Gmodel', 'meno')
    list_display_links = ('brand', 'Gmodel', 'meno','unit', 'type', 'price', 'min_price',)
    list_filter = ('brand', 'type')
    list_per_page = 15
    resource_class = GoodsResources
    model_icon = 'fa fa-map'

    def get_form_layout(self):
        self.form_layout = (
            Main(
                Fieldset('基础信息',
                         'Gmodel',
                         Row('price','min_price')
                         # css_class='unsort no_title'
                         ),
                Fieldset('备注信息',
                        "meno",
                         ),
            ),
            # Side(
            #     Fieldset(_('Status'),
            #              'is_active', 'is_staff', 'is_superuser',
            #              ),
            # )
            Side('选择项目',
                      'brand','supplier','type', 'unit',

                     ),
            )

        return super(GoodsAdmin, self).get_form_layout()


# class GoodsAdmin(object):
#     list_display =['Gmodel', 'unit', 'type', 'price', 'min_price', 'meno',  'supplier']


class SupplierAdmin(object):
    list_display = ['id', 'name', 'tel', 'phone', 'contact', ]
    search_fields = ['name', 'contact']
    list_filter = ['name', 'contact']
    # list_editable =['name','desc']
    model_icon = 'fa fa-users'


class BrandAdmin(object):
    list_display = ['id', 'name', ]
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]
    model_icon = 'fa fa-superpowers '


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Supplier, SupplierAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSittings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
