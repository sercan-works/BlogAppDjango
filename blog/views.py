from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly


class PostList(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    def get(self,request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    #authentication_classes = [SessionAuthentication,BasicAuthentication]
    #permission_classes = [IsOwnerOrReadOnly]
    def get_object(self,pk):
        return get_object_or_404(Post, pk=pk)
    
    def get(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        post = self.get_object(pk)
        post.delete()
        data={
            "message":"Post successfuly deleted..."
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)    
