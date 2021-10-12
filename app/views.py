from django.shortcuts import render, redirect

from .models import Message, Channel, MessageForm


def index(request):
  channels = Channel.objects.all()

  return render(
    request,
    'index.html', {
      'form': MessageForm(),
      'channels': channels,
    }
  )

def channel_view(request, title):
  channel = Channel.objects.get(title=title)
  messages = Message.objects.filter(channel=channel)
  return render(
    request,
    'channel.html', {
      'form': MessageForm(),
      'messages': messages,
      'channel': channel,
    }
  )

def new_message(request, title):
  if request.method != 'POST':
    return redirect('index')
  
  channel = Channel.objects.get(title=title)
  form = MessageForm(request.POST)
  if form.is_valid():
      message = form.save(commit=False)
      message.author = request.user
      message.channel = channel
      message.save()

  return redirect('channel', title=channel.title)
