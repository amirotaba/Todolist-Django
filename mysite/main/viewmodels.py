from django.db import models

#DTO (Data Type Object)
class ResetPassword:
    username = models.CharField(max_length=200)

class GetAnswer:
	answer = models.CharField(max_length=50)

class SetNewPassword:
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

class AddTask:
    task = models.CharField(max_length=200)
