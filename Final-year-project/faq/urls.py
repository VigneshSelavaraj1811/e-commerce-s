from django.urls import path

from . import views

urlpatterns = [
    path('faque', view=views.faq,name='faq'),
 ]
