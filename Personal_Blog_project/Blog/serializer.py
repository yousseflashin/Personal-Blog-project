from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts






class PostsListSerializer(serializers.ModelSerializer):
  
  class Meta:
    model=Posts
    fields=['id','sender_name','time_created','last_updated','title','content']

  sender_name=serializers.StringRelatedField()
  


class CreatePostSerializer(serializers.ModelSerializer):
  class Meta:
    model=Posts
    fields=['title','content']
  
  def save(self,**kwargs):
     sender_name=User.objects.first()
     title=self.validated_data['title']
     content=self.validated_data['content']
     self.instance=Posts.objects.create(sender_name=sender_name,title=title,content=content)


class UpdatePostSerializer(serializers.ModelSerializer):
  class Meta:
    model=Posts
    fields=['title','content']
  
  