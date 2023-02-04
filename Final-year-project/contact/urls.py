from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path('',view=views.contact, name='contact'),

    # url(
    #     regex=_(r'^email_success/$'),
    #     view=views.email_success,
    #     name='email_success'
    # ),
 ]
