from django import forms

class InputForm(forms.Form):
    category = forms.CharField(label='カテゴリー')
    ja_word = forms.CharField(label='日本語')
    en_word = forms.CharField(label='英語')
    memo = forms.CharField(label='メモ')


# from django import forms
#
# from stock.models import StockPurchase
#
#
# class StockPurchaseForm(forms.ModelForm):
#     class Meta:
#         model = StockPurchase
#         fields = ['stock', 'weight', 'email', 'name', ]
#         widgets = {
#             'weight': forms.NumberInput(attrs={'class': 'form-control'}),
#             'stock': forms.RadioSelect(attrs={'class': 'form-check-input'}),
#         }
