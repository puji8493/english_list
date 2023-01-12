from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input_form/', views.form_create_view, name='form_create_view'),
]

