from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm


class custom_user(User):
    class QuestionChoices(models.TextChoices):
        FAVTEAM = 'FV', _('Favorite Team')
        HIGHSCHOOL = 'HN', _('Highschool Nick Name')
    security_question = models.CharField(max_length=2,
            choices = QuestionChoices.choices)
    answer = models.CharField(max_length=50)

class TodoListItem(models.Model):
    text = models.CharField(max_length=200)
    sub_date = models.DateTimeField()
    date_diff = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.CharField(max_length=1)
    def __str__(self):
        return self.text
