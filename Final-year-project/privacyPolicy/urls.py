from django.urls import re_path as url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.privacy,
        name='privacy-policy'
    ),
 ]
