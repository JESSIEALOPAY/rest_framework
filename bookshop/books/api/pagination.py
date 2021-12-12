from rest_framework.pagination import  PageNumberPagination

class SmallPagination(PageNumberPagination):
    page_size= 5


class LargePaagination(PageNumberPagination):
    page_size= 15