from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Posts
from .pagination import DefaultPagination
from .serializer import PostsSerializer
# Create your views here.
class PostView(ModelViewSet):
  queryset=Posts.objects.all()
  serializer_class=PostsSerializer
  pagination_class=DefaultPagination
  search_fields=['title','content']
  def get_serializer_context(self):
      return {'request': self.request}