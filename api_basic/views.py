from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# function based view
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Class based View
# class ArticleList(APIView):
#     def get(self, request):
#         serializer = ArticleSerializer(Article.objects.all(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

# Generic API amd mixins
# class GenericArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class GenericArticleDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Viewset
# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Article.objects.all()
#         serializer = ArticleSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.validated_data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def update(self, request, pk):
#         queryset = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Generic viewset
# class GenericViewSetArticle(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#Model Viewset
class GenericModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
