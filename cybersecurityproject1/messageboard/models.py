from django.db import models
from django.conf import settings

class Message(models.Model):
  content = models.CharField(max_length=300)
  date = models.DateTimeField('sent')
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE)
  def __str__(self) -> str:
      return self.content
