from os import name

from django.contrib import admin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import UserListCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView, UserRegisterCreateApiView

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import PostModelViewSet

router = DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', UserListCreateAPIView.as_view(), name='users'),
    path('user/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('auth/register', UserRegisterCreateApiView.as_view(), name='register'),
    path('', include(router.urls)),
]
