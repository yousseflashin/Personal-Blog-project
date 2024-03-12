from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
  sender_name=models.ForeignKey(User,on_delete=models.CASCADE)
  time_created=models.DateField(auto_now_add=True)
  last_updated=models.DateField(auto_now=True)
  title=models.CharField(max_length=50,blank=False)
  content=models.CharField(max_length=500,blank=False)
