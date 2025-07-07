# chat/models.py
from django.db import models

class Message(models.Model):
    room = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.username}: {self.content}"
