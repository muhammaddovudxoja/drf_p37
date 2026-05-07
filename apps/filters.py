from django_filters import FilterSet, NumberFilter

from apps.models.exammodels import Post


# from apps.models import Product, Book


class PostFilter(FilterSet):
    from_time = NumberFilter(field_name='created_at', lookup_expr='gte')
    to_time = NumberFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ('category', 'tags', 'from_time', 'to_time')

