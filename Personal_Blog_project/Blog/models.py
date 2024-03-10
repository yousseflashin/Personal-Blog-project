from django.db import models
# Create your models here.

class Posts(models.Model):
  sender_name=models.CharField(max_length=30)
  time_created=models.DateTimeField(auto_now_add=True)
  last_updated=models.DateTimeField(auto_now=True)
  title=models.CharField(max_length=50)
  content=models.CharField(max_length=500)
