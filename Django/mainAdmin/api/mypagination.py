from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(CursorPagination):
    page_size = 3
    # page_query_param = 'p'
    # page_size_query_param = 'records'

    ordering = 'city'

  