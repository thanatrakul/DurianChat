from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationDjango(PageNumberPagination):
    page_size_query_param = settings.API_PAGINATE_BY_PARAM
    max_page_size = settings.API_MAX_PAGE_SIZE
