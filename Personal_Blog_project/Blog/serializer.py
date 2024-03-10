from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.Serializer):
  class Meta:
    model=Posts
    fields=['sender','Time_created','last_updated','title','content']
