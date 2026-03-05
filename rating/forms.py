from django import forms
from .models import  Restaurant
class RestaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=("name","score","review")
        labels = {
            'name': '餐廳名稱',
            'score': '評分 (0~5)',
            'review': '評論'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'score': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',   # 允許小數點
                'min': '0',
                'max': '5'
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }