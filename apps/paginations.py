from rest_framework.pagination import PageNumberPagination


class CustomNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'sahifa'
    max_page_size = 100
