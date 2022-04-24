from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import custom_user, TodoListItem
from .viewmodels import GetAnswer, ResetPassword, SetNewPassword, AddTask
from django.forms import ModelForm


# Create your forms here.

class NewUserForm(UserCreationForm):
	class Meta:
		model = custom_user
		fields = ("username", "email", "password1", "password2", "security_question", "answer")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ResetPasswordForm(forms.Form):
	username = forms.CharField(label="Enter your username:", max_length="200")

	class Meta:
		model = ResetPassword
		fields=['username']

class GetAnswerForm(forms.Form):
	answer = forms.CharField(label="Enter your answer: ", max_length=50)

	class Meta:
		model = GetAnswer
		fields =['answer']

class SetNewPasswordForm(forms.Form):
	password1 = forms.CharField(label="Enter password: ", widget=forms.PasswordInput(), max_length=200)
	password2 = forms.CharField(label="ReEnter Password: ", widget=forms.PasswordInput(), max_length=200)

	class Meta:
		model = SetNewPassword
		fields = ['password1', 'password2']

class AddTaskForm(forms.Form):
	task = forms.CharField(label="", max_length="200", widget=forms.TextInput(attrs={'autofocus': 'autofocus', 'id':'task-entry', 'placeholder': 'Your task...'}))

	class Meta:
		model = AddTask
		fields =['task']
