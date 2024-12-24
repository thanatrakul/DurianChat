from .models import FacebookPage
from django.contrib import admin


@admin.register(FacebookPage)
class FacebookPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fields = ('page_id', 'name', 'icon', 'access_token', 'is_active', 'created_at', 'updated_at')

    def icon_preview(self, obj):
        """Displays a small preview of the icon in the admin interface."""
        if obj.icon:
            return f'<img src="{obj.icon.url}" alt="{obj.name}" style="width: 50px; height: 50px; border-radius: 5px;" />'
        return "No Icon"
    icon_preview.allow_tags = True
    icon_preview.short_description = "Icon Preview"
