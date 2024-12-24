from apps.commons.rest_framework.pagination import PageNumberPaginationDjango
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ModelViewsetMixins(ModelViewSet):
    serializer_action_classes = {}
    pagination_class = PageNumberPaginationDjango

    def get_serializer_class(self):
        """
        A class which inhertis this mixins should have variable
        `serializer_action_classes`.
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class SampleViewSet(ActionsModelViewsets):
            serializer_class = DocumentSerializer
            serializer_action_classes = {
               'upload': UploadDocumentSerializer,
               'download': DownloadDocumentSerializer,
            }

            @action
            def upload:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        Default Actions
            - "create" (post)
            - "list" (get)
            - "retrieve" (get)
            - "update" (put)
            - "partial_update" (patch)
        """

        if self.action in self.serializer_action_classes:
            return self.serializer_action_classes[self.action]

        # Default Serializer Class
        return super().get_serializer_class()


class BulkModelViewSetMixin(object):

    def create(self, request, *args, **kwargs):

        # If request.data is list, that it referece for bulk create
        if isinstance(request.data, list):
            return self.bulk_create(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)

    def bulk_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            many=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
