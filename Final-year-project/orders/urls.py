from django.urls import re_path as url
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    url('create/', views.order_create, name='order_create'),
    # url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]
