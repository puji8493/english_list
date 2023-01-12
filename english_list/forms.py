from django import forms
from .models import WordLists

class UserForm(forms.ModelForm):
    class Meta():
        model = WordLists
        fields = '__all__'


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
