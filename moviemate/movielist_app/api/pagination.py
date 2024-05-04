from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class WatchListCPagination(CursorPagination):
    page_size = 2
    ordering = 'created_at'


# PageNumberPagination is mainly used for small datasets
    
# LimitOffsetPagination is used for large datasets
    
# CursorPagination is used for large datasets and when you want to provide a better performance for the user

