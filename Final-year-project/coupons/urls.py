from django.urls import path

from . import views

urlpatterns = [
    path('coupons', view=views.coupon_apply, name='apply'),
]
