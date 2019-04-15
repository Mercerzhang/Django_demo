# 从urls模块中导入url
from django.conf.urls import url


# 从当前目录导入我们的视图模块views
from . import views

urlpatterns = [
    url(r'^req/$', views.req),
    url(r'^form/$', views.form),
    url(r'^geth/$', views.getheadrs),
]