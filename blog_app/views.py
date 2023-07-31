from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogModelSerializer
from .models import Blog
from django.shortcuts import get_object_or_404


class BlogViewSet(viewsets.ViewSet):
     
    def create(self, request):
        serializer = BlogModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        blogs = Blog.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogModelSerializer(blog)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogModelSerializer(data=request.data, instance=blog)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogModelSerializer(data=request.data, instance=blog, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
    
    

    


