from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class AbstractUUID(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name=_("UUID"))

    class Meta:
        abstract = True
