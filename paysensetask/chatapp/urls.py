from django.conf.urls import url
from .views import DeleteAllChatMessages, GetUserIp

urlpatterns = [
    url(r'^delete-all-messages/$', DeleteAllChatMessages.as_view(), name='delete-all-messages'),
    url(r'^get-user-ip/$', GetUserIp.as_view(), name='get-user-ip')

]
