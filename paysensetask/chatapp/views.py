from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from .utils import CustomMetaDataMixin
from django.conf import settings


class ChatMessageViewSet(CustomMetaDataMixin, viewsets.ModelViewSet):
    """
        This is the Merchant CRUD for the admin
    """
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


    def get_queryset(self):
        return ChatMessage.objects.filter(is_active=True).order_by('-created_on')

    def destroy(self, request, *args, **kwargs):
        if not request.data.get('secret_token', None):
            message = "the message can not be deleted 'secret token is not supplied' "
        elif settings.SECRET_TOKEN == request.data.get('secret_token', None):
            instance = self.get_object()
            message = instance.text
            instance.is_active = False
            instance.save()
            message = "message '{0}' has been deleted".format(message)
        else:
            message = "the message can not be deleted 'secret token is not correct' "
        return Response({"message": message})


class DeleteAllChatMessages(CustomMetaDataMixin, generics.DestroyAPIView):
    """
        This API is made to delete all the messages present
    """

    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        return ChatMessage.objects.filter(is_active=True)


    def destroy(self, request, *args, **kwargs):
        if not request.data.get('secret_token', None):
            message = "the message can not be deleted 'secret token is not supplied' "
        elif settings.SECRET_TOKEN == request.data.get('secret_token', None):
            chat_messages = self.get_queryset().update(is_active=False)
            if chat_messages > 0:
                message = "All the messages has been deleted"
        else:
            message = "the message can not be deleted 'secret token is not correct' "
        return Response({"message": message})


class GetUserIp(CustomMetaDataMixin, generics.RetrieveAPIView):
    """
        This API throws back user's ip address
    """

    def retrieve(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return Response({"ip_address": ip})