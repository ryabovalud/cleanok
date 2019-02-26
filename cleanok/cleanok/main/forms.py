from django import forms

class OrderRequestForm(forms.Form):
	# Форма для создания заявки на заказ

	name = forms.CharField(max_length=30, label='Имя')
	phone = forms.CharField(max_length=15, label='Тел. номер')
	email = forms.EmailField(label='Эл. почта')

"""class ReviewForm(forms.Form):
	# Форма для отзыва

	first_name = forms.CharField(max_length=30, label='Имя')
	last_name = forms.CharField(max_length=30, label='Фамилия')
	review_text = forms.CharField(widget=forms.Textarea, label='Отзыв')"""