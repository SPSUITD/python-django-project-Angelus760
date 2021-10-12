from .views import index, channel_view, new_message
from django.urls import path


urlpatterns = [
  path('', index),
  path('<str:title>/', channel_view, name='channel'),
  path('new/<str:title>/', new_message, name='new_message')
]