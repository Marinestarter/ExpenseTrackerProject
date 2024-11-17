from django import forms
from.models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields ='__all__'

        labels = {
            'id': 'Expense ID',
            'name': 'name',
            'amount': 'amount',
            'date': 'date',
            'explanation': 'explanation'
        }

        widgets = {
            'id': forms.NumberInput(attrs={'placeholder': 'eg. 121'}),
            'name': forms.TextInput(attrs={'placeholder': 'Amazon Order'}),
            'amount': forms.NumberInput(attrs={'placeholder': '129'}),
            'date': forms.TextInput(attrs={'placeholder': ''}),
            'explanation': forms.Textarea(attrs={'placeholder': 'Ordered Item1, etc..'}),
        }