from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format="%d %b %y %I:%M %p", read_only=True)

    class Meta:
        model = ChatMessage
        fields = ('id', 'text', 'source_ip', 'created_on')