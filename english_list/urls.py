from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
]
#     path('input_form_page/', views.index,name='index'),