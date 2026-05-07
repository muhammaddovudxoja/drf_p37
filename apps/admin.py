from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from apps.models import User
from apps.models.exammodels import Post


# from apps.models import Post, Comment




@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("first_name", "phone")


@admin.register(Post)
class PottModelAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category", "is_active")
    search_fields = ("title", "description", "price")
    list_filter = ("is_active",)
    ordering = ("-created_at",)


admin.site.unregister(Group)