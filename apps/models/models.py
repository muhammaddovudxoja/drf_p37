#
# from django.contrib.auth.models import AbstractUser
# from django.db.models import IntegerField, CharField, Model, ForeignKey, CASCADE, DecimalField, TextField, \
#     DateTimeField, BooleanField, ManyToManyField, ExpressionWrapper, F, Manager, ImageField
# from django.db.models.constraints import UniqueConstraint
# # class User(Model):
# #     name = models.CharField(max_length=255)
# #     username = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     phone = models.CharField(max_length=50)
# #     website = models.CharField(max_length=100)
# #
# #     address = JSONField()
# #     company = JSONField()k
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # class Post(Model):
# #     user = ForeignKey("apps.User", CASCADE, related_name='posts')
# #     title = CharField(max_length=255)
# #     body = TextField()
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Postlar"
# #
# #
# # class Comment(Model):
# #     post = ForeignKey("apps.Post", CASCADE, related_name='comments')
# #     name = CharField(max_length=255)
# #     email = EmailField(max_length=255)
# #     body = TextField()
# #
# #     def __str__(self):
# #         return self.name
# #
# #     class Meta:
# #         verbose_name_plural = "Kommentlar"
# #
# #
# # class Album(Model):
# #     userId = ForeignKey("apps.User", CASCADE, related_name='albums')
# #     title = CharField(max_length=255)
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Albomlar"
# #
# #
# # class Photo(Model):
# #     title = CharField(max_length=255)
# #     album = ForeignKey("apps.Album", CASCADE, related_name='photos')
# #     url = URLField()
# #     thumbnailUrl = URLField()
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Photolar"
# #
# #
# # class Todo(Model):
# #     user = ForeignKey("apps.User", CASCADE, related_name='todos')
# #     title = CharField(max_length=255)
# #     completed = BooleanField(default=False)
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Todolar"
# #
# #
# # class Book(Model):
# #     title = CharField(max_length=255)
# #     author = CharField(max_length=255)
# #     price = DecimalField(max_digits=10, decimal_places=2)
# #     published_year = IntegerField()
# #     is_available = BooleanField(default=True)
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Kitoblar"
# #
# #
# # class Product(Model):
# #     name = CharField(max_length=255)
# #     price = DecimalField(max_digits=10, decimal_places=2)
# #     stock = IntegerField()
# #
# #     def __str__(self):
# #         return self.name
# #
# #     class Meta:
# #         verbose_name_plural = "Produktlar"
# #
# #
# # class Customer(Model):
# #     name = CharField(max_length=255)
# #     email = EmailField(max_length=255)
# #
# #
# # class Order(Model):
# #     customer = ForeignKey("apps.Customer", CASCADE, related_name='orders')
# #     created_at = DateTimeField(auto_now_add=True)
# #     status = CharField(choices=[("pending", "Pending"), ("completed", "Completed")])
# #
# #
# # class OrderItem(Model):
# #     order = ForeignKey("apps.Order", CASCADE, related_name='items')
# #     product = ForeignKey("apps.Product", CASCADE, related_name='items')
# #     quantity = IntegerField()
#
#
# # class User(AbstractUser):
# #     phone = CharField(max_length=15, null=True, blank=True)
# #
# #
# # class Product(Model):
# #     title = CharField(max_length=255)
# #     description = TextField()
# #     price = DecimalField(max_digits=10, decimal_places=2)
# #     created_at = DateTimeField(auto_now_add=True)
# #     is_active = BooleanField(default=True)
# #     category = ForeignKey("apps.Category", CASCADE, related_name='posts')
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Produktlar"
# #
# #
# # class Category(Model):
# #     title = CharField(max_length=255)
# #
# #     def __str__(self):
# #         return self.title
#
#
# # class Tag(Model):
# #     title = CharField(max_length=255)
# #     posts = ManyToManyField("apps.Post", related_name='tags')
# #
# #     def __str__(self):
# #         return self.title
#
#
# # class Favorite(Model):
# #     product = ForeignKey('apps.Product', CASCADE, related_name='favorites')
# #     user = ForeignKey('apps.User', CASCADE, related_name='favorites')
# #
# #     class Meta:
# #         constraints = [
# #             UniqueConstraint(
# #                 fields=['product', 'user'],
# #                 name='unique_favorite_per_product_per_user'
# #             )
# #         ]
#
#
#
#
#
# # class BookManager(Manager):
# #
# #     def annotate_with_availability(self):
# #         return self.annotate(
# #             available=ExpressionWrapper(
# #                 F('total_copies') - F('borrowed_copies'),
# #                 output_field=IntegerField()
# #             )
# #         )
# #
# #     def available_books(self):
# #         return self.annotate_with_availability().filter(available__gt=0)
# #
# # class Book(Model):
# #     title = CharField(max_length=255)
# #     author = CharField(max_length=255)
# #     price = DecimalField(max_digits=10, decimal_places=2)
# #     published_year = IntegerField()
# #     total_copies = IntegerField()
# #     borrowed_copies = IntegerField()
# #     rating = DecimalField(max_digits=3, decimal_places=1)
# #     image = ImageField(upload_to='books/images', null=True, blank=True)
# #
# #     objects = BookManager()
# #
# #     def __str__(self):
# #         return self.title
# #
# #     class Meta:
# #         verbose_name_plural = "Kitoblar"
#
#
