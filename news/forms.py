from django.forms import ModelForm
from .models import Post, Category
from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(required=True, max_length=128, label='Заголовок', widget=forms.TextInput(attrs={
        'placeholder': 'Заголовок',
        'data-rule': 'minlen:4',
        'data-msg': 'Заголовок должен быть не меньше 4 символов'
    }))

    text = forms.CharField(
        required=True,
        label='Текст',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'data-rule': 'required',
            'placeholder': 'Текст статьи'}))

    type = forms.BooleanField(
        required=False,
        label='Новость?',
        initial=False)

    category = forms.ModelChoiceField(
        required=False,
        empty_label='Выберите категорию',
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
