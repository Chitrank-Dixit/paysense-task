from django.db import models


class TimeStampMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChatMessage(TimeStampMixin):
    """
        ChatMessage stored the message post on the chatbot with timestamp
    """
    text = models.CharField(max_length=400)
    source_ip = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "chatapp"

    def __str__(self):
        return self.message