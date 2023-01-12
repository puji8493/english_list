from django.shortcuts import render
from django.http import HttpResponse
from .models import WordLists
from . import forms

def index(request):
    data = WordLists.objects.all()
    params = {
        'title':'english_lists',
        'message':'忘れないようにすることをメモ',
        'data':data
    }
    return render(request,'english_list/index.html',params)

def form_create_view(request):
    form = forms.UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'english_list/form_create_view.html',{'form':form})

