from django.db.models import Exists, OuterRef, Value, BooleanField
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.filters import PostFilter
from apps.models import User
from apps.models.exammodels import Post, Like
from apps.permissions import IsAuthor, CustomPostPermission
from apps.serializers import UserModelSerializer, UserRegisterSerializer, PostModelSerializer


@extend_schema(tags=['users'])
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['users'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['users'])
class UserRegisterCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=['posts'])
class PostListCreateAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = PostFilter
    search_fields = ('title', 'content')
    ordering_fields = ('created_at', 'views_count')
    permission_classes = [IsAuthenticated, IsAuthor, CustomPostPermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.is_authenticated:
            key = Exists(Like.objects.filter(product_id=OuterRef('pk'), user=user))
        else:
            key = Value(False, BooleanField())

        return qs.annotate(
            likes_count=Count('favorites'),
            is_liked=key
        )





#
# @extend_schema(tags=["posts"])
# class PostCommentListAPIView(ListAPIView):
#     queryset = Comment.objects.order_by("-id")
#     serializer_class = CommentModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get("pk")
#         return qs.filter(post_id=pk)
#
#
# @extend_schema(tags=["comments"])
# class CommentListCreateAPIView(ListCreateAPIView):
#     queryset = Comment.objects.order_by("-id")
#     serializer_class = CommentModelSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_fields = ['email', 'post__id']
#     search_fields = ['name','email', 'body']
#     ordering_fields = ['id', 'post__id']
#
# @extend_schema(tags=["comments"])
# class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentModelSerializer
#
#
# @extend_schema(tags=["albums"])
# class AlbumListCreateAPIView(ListCreateAPIView):
#     queryset = Album.objects.order_by("-id")
#     serializer_class = AlbumModelSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_class = AlbumFilter
#     search_fields = ('title', )
#     ordering_fields = ['id', 'userId']
#
#
# @extend_schema(tags=["albums"])
# class AlbumRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumModelSerializer
#
# @extend_schema(tags=["albums"])
# class AlbumPhotoListAPIView(ListAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get("pk")
#         return qs.filter(album_id=pk)
#
# @extend_schema(tags=["photos"])
# class PhotoListCreateAPIView(ListCreateAPIView):
#     queryset = Photo.objects.order_by("-id")
#     serializer_class = PhotoModelSerializer
#
#
# @extend_schema(tags=["photos"])
# class PhotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoModelSerializer
#
# @extend_schema(tags=["todos"])
# class TodoListCreateAPIView(ListCreateAPIView):
#     queryset = Todo.objects.order_by("-id")
#     serializer_class = TodoModelSerializer
#
#
# @extend_schema(tags=["todos"])
# class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.order_by("-id")
#     serializer_class = TodoModelSerializer
#
#
# @extend_schema(tags=["users"])
# class UserListCreateAPIView(ListCreateAPIView):
#     queryset = User.objects.order_by("-id")
#     serializer_class = UserModelSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_fields = ['name', "id"]
#     search_fields = ['name', "phone", 'address']
#     ordering_fields = ['id', 'name']
#
#
#
# @extend_schema(tags=["users"])
# class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.order_by("-id")
#     serializer_class = UserModelSerializer
#
#
# @extend_schema(tags=["users"])
# class UserPostListAPIView(ListAPIView):
#     queryset = Post.objects.order_by("-id")
#     serializer_class = PostModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get("pk")
#         return qs.filter(user_id=pk)
#
#
# @extend_schema(tags=["users"])
# class UserAlbumListAPIView(ListAPIView):
#     queryset = Album.objects.order_by("-id")
#     serializer_class = AlbumModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get("pk")
#         return qs.filter(user_id=pk)
#
#
# @extend_schema(tags=["users"])
# class UserTodoListAPIView(ListAPIView):
#     queryset = Todo.objects.order_by("-id")
#     serializer_class = TodoModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get("pk")
#         return qs.filter(user_id=pk)
#
#
# @extend_schema(tags=["Kitoblar"])
# class BookListCreateAPIView(ListCreateAPIView):
#     queryset = Book.objects.order_by("-id")
#     serializer_class = BookModelSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_class = BookFilter
#     search_fields = ('title', )
#     ordering_fields = ['id', 'title']
#
# @extend_schema(tags=["Kitoblar"])
# class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer

# @extend_schema(tags=['products'])
# class ProductListCreateAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# @extend_schema(tags=['products'])
# class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# @extend_schema(tags=['customers'])
# class CustomerListCreateAPIView(ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
# @extend_schema(tags=['customers'])
# class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
# @extend_schema(tags=['orders'])
# class OrderListCreateAPIView(ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
# @extend_schema(tags=['orders'])
# class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
# @extend_schema(tags=['ordersItems'])
# class OrderItemListCreateAPIView(ListCreateAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#
# @extend_schema(tags=['ordersItems'])
# class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer




#
#
# @extend_schema(tags=['products'])
# class ProductListCreateAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_class = ProductFilter
#     search_fields = ('title',)
#     ordering_fields = ('created_at',)
#     permission_classes = [IsAuthenticated, IsAuthor]
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         user = self.request.user
#
#         if user.is_authenticated:
#             key = Exists(Favorite.objects.filter(product_id=OuterRef('pk'), user=user))
#         else:
#             key = Value(False, BooleanField())
#
#         return qs.annotate(
#             favorite_count=Count('favorites'),
#             is_favorite=key
#         )
#
#
# @extend_schema(tags=['products'])
# class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#     permission_classes = [IsAuthenticated, IsAuthor]
#
#
#
# @extend_schema(tags=['books'])
# class BookListCreateAPIView(ListCreateAPIView):
#     queryset = Book.objects.annotate_with_availability()
#     serializer_class = BookModelSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_class = BookFilter
#     search_fields = ('title',)
#     ordering_fields = ['rating', 'published_year', 'title', 'total_copies']
#
#     def get_queryset(self):
#         return self.queryset.annotate_with_availability()
#
# @extend_schema(tags=['books'])
# class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.annotate_with_availability()
#     serializer_class = BookModelSerializer
#
#     def get_queryset(self):
#         return self.queryset.annotate_with_availability()
#


#
#
#
# from django.db.models import OuterRef, Exists
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.generics import CreateAPIView
# from rest_framework.viewsets import ModelViewSet
# from drf_spectacular.utils import extend_schema
#
# from apps.models import Book, Course, Enrollment, Lesson
# from apps.permissions import IsCourseOwnerOrEnrolled
# from apps.serializers import BookSerializer, CourseSerializer, LessonSerializer, UserSerializer
#
#
# @extend_schema(tags=('Book',))
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.annotate_with_availability()
#     serializer_class = BookSerializer
#
#     filter_backends = (SearchFilter, OrderingFilter)
#     search_fields = ('title', 'author__username')
#     ordering_fields = ('price', 'published_year')
#     ordering = ('-published_year', 'price')
#
#
# @extend_schema(tags=('Course',))
# class CourseViewSet(ModelViewSet):
#     serializer_class = CourseSerializer
#
#     def get_queryset(self):
#         queryset = Course.objects.all()
#         user = self.request.user
#
#         if user.is_authenticated:
#             unfinished = Enrollment.objects.filter(
#                 user=user,
#                 course=OuterRef('pk'),
#                 is_completed=False
#             )
#
#             if self.request.query_params.get('unfinished') == 'true':
#                 queryset = queryset.filter(Exists(unfinished))
#
#             queryset = queryset.annotate(is_unfinished=Exists(unfinished))
#
#         return queryset
#
#
# @extend_schema(tags=('Lesson',))
# class LessonViewSet(ModelViewSet):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#     permission_classes = (IsCourseOwnerOrEnrolled,)
#



















