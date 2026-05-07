# from django.db.models import Model, ForeignKey, CASCADE
# from django.db.models.fields import CharField, DecimalField, IntegerField, PositiveIntegerField, BooleanField
#
#
# from apps.models.managers import BookManager
#
#
# class Book(Model):
#     title = CharField(max_length=75)
#     author = ForeignKey('apps.User', related_name='books', on_delete=CASCADE)
#     price = DecimalField(max_digits=10, decimal_places=2)
#     published_year = IntegerField()
#     total_copies = PositiveIntegerField(default=1)
#     borrowed_copies = PositiveIntegerField(default=0)
#     is_available = BooleanField(default=True)
#
#     objects = BookManager()
#
#     def str(self):
#         return self.title