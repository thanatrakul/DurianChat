from apps.commons.abstracts.models import AbstractUUID
from apps.commons.softdelete.models import SoftDeleteModel
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class ControlModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_user",
        verbose_name=_('Created User')
    )
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated_user",
        verbose_name=_('Edited User')
    )

    class Meta:
        abstract = True


class SoftControlModel(AbstractUUID, ControlModel, SoftDeleteModel):

    class Meta:
        abstract = True

    def unique_error_message(self, model_class, unique_check):
        unique_check_list = list(unique_check)
        unique_check = tuple(field for field in unique_check_list if field != "is_deleted")
        # unique_check = tuple(field for field in unique_check_list if field != "live")
        return super(SoftControlModel, self).unique_error_message(model_class, unique_check)


class HardControlModel(AbstractUUID, ControlModel):

    class Meta:
        abstract = True
