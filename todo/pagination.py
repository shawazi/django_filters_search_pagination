from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 25
    
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 25
    
class MyCursorPagination(CursorPagination):
    page_size = 15
    ordering = "id"