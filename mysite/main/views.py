from django.shortcuts import  render, redirect
from .forms import NewUserForm, ResetPasswordForm, GetAnswerForm
from .forms import SetNewPasswordForm, AddTaskForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import custom_user, TodoListItem
from django.shortcuts import get_object_or_404
from datetime import date

def homepage(request):
	if(request.method == "POST"):
		if "delete" in request.POST:
			pk = request.POST["delete"]
			record = TodoListItem.objects.get(pk = pk)
			record.delete()
			return redirect("main:homepage")
		elif "check" in request.POST:
			pk = request.POST["check"]
			record = TodoListItem.objects.filter(pk = pk)
			record.update(done = "Y")
			return redirect("main:homepage")
		else:
			form = AddTaskForm(request.GET)
			id = request.user.id
			list = TodoListItem.objects.filter(user_id=id)
			now = date.today()
			TodoListItem.objects.create(text = request.POST['task'],
			 sub_date = now, user_id = id, date_diff = 0)
			main_list = TodoListItem.objects.filter(user_id=id)
			main_list = main_list.values_list("text",
			 "sub_date", "done", "date_diff", "pk")
			diff_list = []
			diff_date(main_list)
			for dif in diff_list:
				print(dif)
			return render(request=request, template_name='main/home.html',
			 context={"addtask_form":form, "mainlist":main_list})
	elif(request.method == "GET"):
		form = AddTaskForm(request.GET)
		id = request.user.id
		main_list = TodoListItem.objects.filter(user_id=id)
		main_list = main_list.values_list("text",
		 "sub_date", "done", "date_diff", "pk")
		diff_list = []
		diff_date(main_list)
		now = date.today()
		return render(request=request, template_name='main/home.html',
		 context={"addtask_form":form,"mainlist":main_list})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		# print(form)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request,
		 "Unsuccessful registration.Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html",
	 context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request,
				 f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html",
	 context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("main:login")


def resetpassword_request(request):
	if(request.method == "POST"):
		form = ResetPasswordForm(request.POST)
		if(request.POST["username"] != None):
			username = request.POST["username"]
			try:
				user = custom_user.objects.get(username = username)
				quest = user.get_security_question_display()
				answer = user.answer
				formans = GetAnswerForm(request.POST)
				request.session['answer'] = answer
				request.session['question'] = quest
				request.session['username'] = username
				return redirect('main:getanswer')
			except Exception:
				messages.error(request, "User not found!")
				form = ResetPasswordForm(request.GET)
				return render(request = request,
				 template_name = 'main/auth/resetpassword.html',
				  context={"resetpassword_form": form})
	elif(request.method == "GET"):
		form = ResetPasswordForm(request.GET)
		return render(request = request,
		 template_name = 'main/auth/resetpassword.html',
		  context={"resetpassword_form": form})


def getanswer_request(request):
	if(request.method == "POST"):
		useranswer = request.POST["answer"]
		# print("User: " + useranswer)
		correctAnswer = request.session["answer"]
		# print("Correct: " + correctAnswer)
		if(useranswer == correctAnswer):
			form = SetNewPasswordForm(request.POST)
			return redirect('main:setnewpassword')
		else:
			messages.error(request, "Answer is wrong :(")
			return redirect('main:resetpassword')
	else:
		quest = request.session["question"]
		form = GetAnswerForm(request.POST)
		return render(request = request,
		 template_name = 'main/auth/getanswer.html',
		  context={"getanswer_form": form, "question":quest})


def setnewpassword_request(request):
	if(request.method == "POST"):
		username = request.session["username"]
		user = custom_user.objects.get(username = username)
		user.set_password(request.POST['password1'])
		user.save()
		messages.info(request, "Password Successfully changed!")
		form = AuthenticationForm()
		return redirect('main:login')
	else:
		form = SetNewPasswordForm(request.POST)
		return render(request = request,
		 template_name = 'main/auth/setnewpassword.html',
		  context={"setnewpassword_form": form})

def diff_date(main_list):
	now = date.today()
	for day in main_list:
		diff = now - (day[1].date())
		record = TodoListItem.objects.filter(sub_date=day[1])
		record.update(date_diff=diff.days)
