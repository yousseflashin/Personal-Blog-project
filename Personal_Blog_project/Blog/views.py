from django.shortcuts import render
from rest_framework import response,decorators,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAdminUser,DjangoModelPermissions
from .models import Posts
from .pagination import DefaultPagination
from .serializer import PostsListSerializer,CreatePostSerializer,UpdatePostSerializer
# Create your views here.
class PostView(ModelViewSet):
  queryset=Posts.objects.all()
  serializer_class=PostsListSerializer
  pagination_class=DefaultPagination
  search_fields=['title','content']
  http_method_names =['get','delete','put','post']

  def get_permissions(self):
      if self.request.method == 'GET':
        return [AllowAny()]
      return [IsAdminUser()]
  def get_serializer_class(self):
      if self.request.method == 'POST':
         return CreatePostSerializer
      elif self.request.method=='PUT':
         return UpdatePostSerializer
      return PostsListSerializer
  
  def create(self,request,*args,**kwargs):
      serializer=CreatePostSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return response.Response(serializer.data)