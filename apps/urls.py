from os import name

from django.contrib import admin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import UserListCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView, UserRegisterCreateApiView
#
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', UserListCreateAPIView.as_view(), name='users'),
    path('user/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('auth/register', UserRegisterCreateApiView.as_view(), name='register')


#     # path('prodducts', ProductListCreateAPIView.as_view(), name='products'),
#     # path('products/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product'),
#     # path('books', BookListCreateAPIView.as_view(), name='books'),
#     # path('books/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view(), name='book'),

]


#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# from apps.views import BookViewSet, CourseViewSet, LessonViewSet, UserCreateView
#
# router = DefaultRouter()
# router.register('books', BookViewSet)
# router.register('courses', CourseViewSet, basename='courses')
# router.register('lessons', LessonViewSet, basename='lessons')
#
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('auth/register', UserCreateView.as_view()),
# ]





















