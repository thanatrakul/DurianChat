from apps.commons.mongodb.pagination import MongoLimitOffsetPagination
from rest_framework_mongoengine.viewsets import ModelViewSet


class MongoModelViewsetMixins(ModelViewSet):
    pagination_class = MongoLimitOffsetPagination
