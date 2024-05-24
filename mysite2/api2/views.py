from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import *
from .serializers import *
from blog.models import *
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
# 
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PostLikeAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {'like': instance.like+1}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(data['like'])
    
    

class CateTagAPIView(APIView):
    def get(sefl, reqeust, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        data = {
            'cateList' : cateList,
            'tagList' : tagList
        }

        serializer = CateTagSerializer(instance=data)
        return Response(serializer.data)
    
from rest_framework.generics import GenericAPIView

class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)
    
    
from rest_framework.pagination import PageNumberPagination

class PostPangeNumberPagination(PageNumberPagination):
    page_size = 3
    # def get_paginated_response(self, data):        
        # return Response(OrderedDict([
            # ('pagCnt', self.page.paginator.num_pages),
            # ('curPage', self.page.number),          
            # ('postList', data)
        # ]))
        # 
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPangeNumberPagination