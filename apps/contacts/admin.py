from .models import Contact
from django.contrib import admin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("page", 'name', 'user_id', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'user_id')              # Enable search on specific fields
    list_filter = ('created_at',)                        # Enable filtering by specific fields
    ordering = ('-created_at',)                          # Default ordering (newest first)
    readonly_fields = ('user_id', 'created_at')                   # Make specific fields read-only

    fieldsets = (
        (None, {
            'fields': ('name', 'user_id', 'profile_picture')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
        }),
    )
