from django.urls import path

from .views import index, room, chat_send, chat_list

urlpatterns = [
    path('', index, name='index'),
    path('<slug:room_name>/', room, name='room'),
    path('<slug:room_name>/send', chat_send, name='send'),
    path('<slug:room_name>/list', chat_list, name='send_list')
]