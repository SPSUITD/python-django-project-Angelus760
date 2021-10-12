from django.db import models
from django import forms
from django.contrib.auth import get_user_model


User_model = get_user_model()


class Channel(models.Model):
  title = models.CharField(max_length=100)


class Message(models.Model):
  channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
  author = models.ForeignKey(User_model, on_delete=models.CASCADE)
  text = models.CharField(max_length=500)
  pub_date = models.DateTimeField(auto_now_add=True)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('author', 'channel')
