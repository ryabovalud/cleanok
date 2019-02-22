from django import forms

class OrderRequestForm(forms.Form):

	name = forms.CharField('Имя', max_length=30)
	phone = forms.CharField('Телефон', max_length=15)
	email = forms.EmailField('E-Mail')

class ReviewForm(forms.Form):

	first_name = forms.CharField('Имя', max_length=30)
	last_name = forms.CharField('Фамилия', max_length=30)
	review_text = forms.TextField('Текст отзыва')