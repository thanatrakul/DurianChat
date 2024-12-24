from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination


class NoCountPaginator(Paginator):

    @property
    def count(self):
        return 0


class MongoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
