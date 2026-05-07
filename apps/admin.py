from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from apps.models import User
from apps.models.exammodels import Post, Like

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("first_name", "phone")


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0


@admin.register(Post)
class PottModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'created_at', 'author', 'views_count')
    search_fields = ("title",)
    list_filter = ("views_count",)
    ordering = ("-created_at",)
    readonly_fields = ("views_count",)
    inlines = [LikeInline]


admin.site.unregister(Group)