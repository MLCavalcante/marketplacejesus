from django import forms

from .models import Item


IMPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
    
        widgets = {
            'category': forms.Select(attrs={
            'class': IMPUT_CLASS,
             }),
             'name': forms.TextInput(attrs={
             'class': IMPUT_CLASS,
             }),
             'description': forms.Textarea(attrs={
             'class': IMPUT_CLASS,
             }),
             'price': forms.TextInput(attrs={
             'class': IMPUT_CLASS,
             }),
             'image': forms.FileInput(attrs={
             'class': IMPUT_CLASS,
             }),
         
         
         
         }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold',)
    
        widgets = {
             'name': forms.TextInput(attrs={
             'class': IMPUT_CLASS,
             }),
             'description': forms.Textarea(attrs={
             'class': IMPUT_CLASS,
             }),
             'price': forms.TextInput(attrs={
             'class': IMPUT_CLASS,
             }),
             'image': forms.FileInput(attrs={
             'class': IMPUT_CLASS,
             }),
         
         
         }

    