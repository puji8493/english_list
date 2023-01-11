from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import InputForm
from .models import WordLists

def index(request):
    data = WordLists.objects.all()
    params = {
        'title':'english_words',
        'message':'all wordlists',
        'data':data
    }
    return render(request,'english_list/index.html',params)



# def index(request):
#     dic = {'day' :datetime.today(),
#            'weather':"晴れ"}
#     return render(request,'english_list/index.html',dic)

# def index(request):
#     params = {
#         'title':'english_word_lists',
#         'message':'リスト登録フォーム',
#         'form':InputForm
#     }
#     if (request.method == 'POST'):
#         params['message'] = 'カテゴリー：' + request.POST['category'] + '<br>日本語：' + request.POST['ja_word'] + '<br>英語：' + request.POST['en_word'] + '<br>メモ：' + request.POST['memo']
#         params['form'] = InputForm(request.POST)
#     return render(request,'english_list/index.html',params)

# render 描画する関数　戻り値を受取って描画する
# 直接文字だけ表示なら return HttpResponse('文字列')