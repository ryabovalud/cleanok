from django import forms

class OrderRequestForm(forms.Form):

	name = forms.CharField(max_length=30, label='Имя')
	phone = forms.CharField(max_length=15, label='Тел. номер')
	email = forms.EmailField(label='Эл. почта')

class ReviewForm(forms.Form):

	first_name = forms.CharField(max_length=30, label='Имя')
	last_name = forms.CharField(max_length=30, label='Фамилия')
	review_text = forms.CharField(widget=forms.Textarea, label='Отзыв')