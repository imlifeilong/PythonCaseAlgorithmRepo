from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Book
from app.serializers import BookSerializer

"""
pagination_class属性仅支持在genericsAPIView和视图集viewset中配置使用。
如果你使用函数或简单的APIView开发API视图，那么你需要对你的数据进行手动分页
"""


class BookAPIView(APIView):
    def get(self, request):
        objects = Book.objects.all()
        serializer = BookSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from django.core.paginator import Paginator
from rest_framework import status, mixins, generics

"""
http://127.0.0.1:8000/book-django-paginator-api-view/?page=5

使用 Django 内置的 Paginator 类
首先在视图函数中导入Paginator类：from django.core.paginator import Paginator。
然后在get方法中获取所有的书籍数据，假设你有一个Book模型，并且通过Book.objects.all()获取了所有书籍的查询集books_queryset。
接着创建Paginator对象，指定每页显示的数量，例如每页显示 10 条数据：paginator = Paginator(books_queryset, 10)。
从请求的查询参数中获取当前页码，默认为 1：page_number = int(request.GET.get('page', 1))。
获取当前页的书籍数据：page_obj = paginator.get_page(page_number)。

"""


class BookDjangoPaginatorAPIView(APIView):
    def get(self, request):
        objects = Book.objects.all()
        paginator = Paginator(objects, 10)
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)
        serializer = BookSerializer(page_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

"""
http://127.0.0.1:8000/book-drf-pagination-api-view/?page=5
DRF 提供了几种内置的分页类，如PageNumberPagination、LimitOffsetPagination等。这里以PageNumberPagination为例

"""


class CustomCursorPagination(CursorPagination):
    """
    翻页方式加密的
    http://127.0.0.1:8000/book-list-api-view/?cursor=cD01Mw%3D%3D
    """
    page_size = 10
    ordering = 'id'
    cursor_query_param = 'cursor'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    翻页方式
    http://127.0.0.1:8000/book-list-api-view/?limit=5&offset=10
    """
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100


class CustomPageNumberPagination(PageNumberPagination):
    """
    翻页方式
    http://127.0.0.1:8000/book-list-api-view/?page=5
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookDRFPaginationAPIView(APIView):
    def get(self, request):
        books_queryset = Book.objects.all()
        paginator = CustomPageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(books_queryset, request)
        serializer = BookSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

"""
继承通用视图类
"""


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookMixinGenericAPIView(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    # 用一个视图集替代ArticleList和ArticleDetail两个视图
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination
