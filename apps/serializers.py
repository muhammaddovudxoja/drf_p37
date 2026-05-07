from datetime import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, HiddenField, CurrentUserDefault, CharField, IntegerField, \
    ListField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, Serializer, ListSerializer
from unicodedata import category

from apps.models import User
from apps.models.exammodels import Post, Tag


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "username", "password", "email", "phone"


class UserRegisterSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = "id", "username", 'first_name', 'last_name', 'email', 'phone', 'password', 'confirm_password'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_phone(self, value: str):
        if not len(value) <= 15 and value.isdigit() and value.startswith('+998'):
            raise ValidationError(
                "Telefon raqamingizni to'g'ri kiiriting!"
            )
        return value

    def validate(self, attrs):
        if attrs.pop('confirm_password') != attrs.get('password'):
            raise ValidationError(
                'Parolni tasdiqlashda xato!'
            )
        return attrs

    def create(self, *args, **kwargs):
        return User.objects.create(**self.validated_data)

class PostModelSerializer(ModelSerializer):
    tags = ListField(write_only=True, required=False)
    tag_names = SlugRelatedField(source='tags', many=True, read_only=True, slug_field='name')
    author = HiddenField(default=CurrentUserDefault())
    likes_count = SerializerMethodField()
    is_liked = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'created_at', 'author', 'views_count', 'tags', 'tag_names']
        extra_kwargs = {
            'views_count': {'read_only': True},
            'likes_count': {'read_only': True},
        }


    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        return obj.likes.filter(id=self.context['request'].user.id).exists()

    def _get_or_create_tags(self, tags_data):
        tag_objects = []
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip().lower())
            tag_objects.append(tag)
        return tag_objects

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(self._get_or_create_tags(tags_data))
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        instance = super().update(instance, validated_data)
        if tags_data is not None:
            instance.tags.set(self._get_or_create_tags(tags_data))

        return instance














# #
# # class CommentModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Comment
# #         fields = '__all__'
# #
# #
# # class AlbumModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Album
# #         fields = ['userId', 'id', 'title']
# #
# #
# # class PhotoModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Photo
# #         fields = '__all__'
# #
# #
# # class TodoModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Todo
# #         fields = '__all__'
# #
# #
# # class UserModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = '__all__'
# #
# #
# # class BookModelSerializer(ModelSerializer):
# #     is_expensive = SerializerMethodField()
# #
# #     class Meta:
# #         model = Book
# #         fields = ('title', 'author', 'published_year', 'is_expensive')
# #
# #     def validate_price(self, val):
# #         if val <= 0:
# #             raise ValidationError("Narxni to'g'ri kiriting!")
# #         return val
# #
# #     def validate_published_year(self, val):
# #         if val < 1900 or val >= now().year:
# #             raise ValidationError("Tug'ilgan sanangizni to'g'ri kiriting!")
# #         return val
# #
# #     def get_is_expensive(self, obj: Book):
# #         return obj.price > 100
# #
# #     def validate(self, attrs):
# #         if attrs['author'] == attrs['title']:
# #             raise ValidationError("Avtor ismi bilan kitobning nomi bir xil bo'lmasligi kerak!")
# #         return attrs
# #
# #

# #
# # class CategoryModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Category
# #         fields = 'title'
# #
# #
# # class ProductModelSerializer(ModelSerializer):
# #     # author = HiddenField(default=CurrentUserDefault())
# #     favorites_count = SerializerMethodField()
# #     is_favorited = SerializerMethodField()
# #
# #     class Meta:
# #         model = Product
# #         fields = "title", "description", "category", "favorites_count", "is_favorited"
# #         read_only_fields = ('category',)
# #
# #     def get_favorites_count(self, obj):
# #         return obj.favorites.count()
# #
# #     def get_is_favorited(self, obj):
# #         return obj.is_favorite
# #
# #
# # class BookModelSerializer(ModelSerializer):
# #     is_classic = SerializerMethodField()
# #     available = SerializerMethodField()
# #
# #     class Meta:
# #         model = Book
# #         fields = [
# #             'id',
# #             'title',
# #             'author',
# #             'published_year',
# #             'rating',
# #             'total_copies',
# #             'borrowed_copies',
# #             'available',
# #             'is_classic',
# #             'image',
# #         ]
# #
# #     def get_is_classic(self, obj: Book) -> bool:
# #         current_year = datetime.now().year
# #         return (current_year - obj.published_year) >= 10
# #
# #     def validate_publication_year(self, value):
# #         current_year = datetime.now().year
# #         if value > current_year:
# #             raise ValidationError(
# #                 f"Nashr yili {current_year} dan katta bo'lishi mumkin emas."
# #             )
# #         if value < 1000:
# #             raise ValidationError(
# #                 "Nashr yili 1000 dan kichik bo'lishi mumkin emas."
# #             )
# #         return value
# #
# #     def validate(self, attrs):
# #         total = attrs.get('total_copies', 0)
# #         borrowed = attrs.get('borrowed_copies', 0)
# #         if borrowed > total:
# #             raise ValidationError({
# #                 'borrowed_copies': (
# #                     f"Berilgan nusxalar ({borrowed}) jami "
# #                     f"nusxalar ({total}) dan oshib ketdi."
# #                 )
# #             })
# #         return attrs
# #
# #

# #
# # class CustomerSerializer(ModelSerializer):
# #     class Meta:
# #         model = Customer
# #         fields = '__all__'
# #
# #
# # class OrderItemSerializer(ModelSerializer):
# #     class Meta:
# #         model = OrderItem
# #         exclude = ('order', )
# #
# #
# # class OrderSerializer(ModelSerializer):
# #     items = OrderItemSerializer(many=True)
# #     total_price = SerializerMethodField()
# #     total_items = SerializerMethodField()
# #
# #     class Meta:
# #         model = Order
# #         fields = ("id", "customer", "items", "total_price", 'total_items')
# #
# #     def create(self, validated_data):
# #         customer = validated_data.pop('customer')
# #         items = validated_data.pop("items")
# #         order = Order.objects.create(customer=customer)
# #         for item in items:
# #             product = item["product"]
# #             quantity = item["quantity"]
# #             if product.stock < quantity:
# #                 raise ValidationError("Prudukt yetarli emas!!!")
# #             product.stock -= quantity
# #             product.save()
# #             OrderItem.objects.create(order=order, product=product, quantity=quantity)
# #
# #         return order
# #
# #     def update(self, instance, validated_data):
# #         items = validated_data.pop("items")
# #
# #         for old_item in instance.items.all():
# #             product = old_item["product"]
# #             product.stock += old_item["quantity"]
# #             product.save()
# #
# #         instance.items.all().delete()
# #
# #         for new_item in items:
# #             product = new_item["product"]
# #             quantity = new_item["quantity"]
# #             if product.stock < quantity:
# #                 raise ValidationError("Prudukt yetarli emas!!!")
# #             product.stock -= quantity
# #             product.save()
# #
# #         return instance
# #
# #     def validate(self, attrs):
# #         items = attrs.get("items")
# #         if not items:
# #             raise ValidationError("Iplos hackerr!!!")
# #         return attrs
# #
# #     def validate_items(self, items):
# #         created = []
# #         for item in items:
# #             product = item["product"]
# #             if product in created:
# #                 raise ValidationError("Bitta narsani ikki martta qo'shma!")
# #             created.append(product)
# #         return items
# #
# #     def get_total_price(self, obj):
# #         total_price = 0
# #         for item in obj.items.all():
# #             total_price += item.product.price * item.quantity
# #         return total_price
# #
# #     def get_total_items(self, obj):
# #         return obj.items.all().count()
# # from apps.models import Book, Lesson, Course, User
# #
# #
# # class BookSerializer(ModelSerializer):
# #     available_copies = IntegerField(read_only=True)
# #
# #     is_expensive = SerializerMethodField()
# #     is_classic = SerializerMethodField()
# #
# #     class Meta:
# #         model = Book
# #         fields = ('id', 'title', 'author', 'price', 'published_year', 'total_copies', 'borrowed_copies',
# #                   'available_copies', 'is_available', 'is_expensive', 'is_classic')
# #
# #     def validate_price(self, value):
# #         if value < 0:
# #             raise ValidationError("Narx 0 dan kichik bo'lishi mumkin emas.")
# #         return value
# #
# #     def validate_published_year(self, value):
# #         if value < 1900:
# #             raise ValidationError("Yili 1900 dan kichik bo'lishi mumkin emas.")
# #         return value
# #
# #     def validate(self, data):
# #         if data.get('title') == str(data.get('author')):
# #             raise ValidationError("Kitob nomi va muallifi bir xil bo'lishi mumkin emas.")
# #         return data
# #
# #     def get_is_expensive(self, obj):
# #         return obj.price > 100
# #
# #     def get_is_classic(self, obj):
# #         current_year = date.today().year
# #         return (current_year - obj.published_year) >= 10
# #
# #
# # class LessonSerializer(ModelSerializer):
# #     class Meta:
# #         model = Lesson
# #         fields = ('id', 'course', 'title', 'content', 'order', 'is_preview')
# #
# # class CourseSerializer(ModelSerializer):
# #     is_unfinished = BooleanField(read_only=True)
# #
# #     class Meta:
# #         model = Course
# #         fields = ('id', 'title', 'description', 'instructor', 'is_published', 'is_unfinished')





































