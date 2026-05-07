from django.db.models import Model, CharField, ForeignKey, TextField, CASCADE, ManyToManyField, DateTimeField, \
    IntegerField
from django.db.models.constraints import UniqueConstraint


class Category(Model):
    name = CharField(max_length=13, unique=True)
    slug = CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Tag(Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"


class Post(Model):
    author = ForeignKey("apps.User", CASCADE, related_name='posts')
    category = ForeignKey("apps.Category", CASCADE, related_name='posts')
    tags = ManyToManyField("apps.Tag", related_name='posts')
    title = CharField(max_length=255)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    views_count = IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Postlar"


class Like(Model):
    user = ForeignKey("apps.User", CASCADE, related_name='likes')
    post = ForeignKey("apps.Post", CASCADE, related_name='likes')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['post', 'user'],
                name='unique_like_per_post_per_user'
            )
        ]
