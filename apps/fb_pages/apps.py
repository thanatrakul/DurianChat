from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FbPagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.fb_pages"
    verbose_name = _("Facebook Pages")
