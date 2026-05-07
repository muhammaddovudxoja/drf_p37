from django_filters import FilterSet, NumberFilter

from apps.models.exammodels import Post


# from apps.models import Product, Book


class PostFilter(FilterSet):
    from_time = NumberFilter(field_name='created_at', lookup_expr='gte')
    to_time = NumberFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ('category', 'tags', 'from_time', 'to_time')










#
#
#
# class AlbumFilter(FilterSet):
#     class Meta:
#         model = Album
#         fields = ('userId', 'title')
#
# class BookFilter(FilterSet):
#     class Meta:
#         model = Book
#         fields = ('title', )

# class ProductFilter(FilterSet):
#     from_ = NumberFilter(field_name='created_at', lookup_expr='gte')
#     to = NumberFilter(field_name='created_at', lookup_expr='lte')
#
#     # comment_count = NumberFilter(method='filter_comment_count')
#     class Meta:
#         model = Product
#         fields = ('from_', 'to')
#
#     # def filter_comment_count(self, queryset, key, value):
#     #     return  queryset.annotate(comment_count=Count('comments')).filter(comment_count__gte=value)
#
#
# class BookFilter(FilterSet):
#     class Meta:
#         model = Book
#         fields = ("published_year",)

















