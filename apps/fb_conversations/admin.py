from .models import Conversation
from django.contrib import admin


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('contact', 'message', 'timestamp')  # Fields to display in the list view
    search_fields = ('contact__name', 'message')        # Enable search on specific fields
    list_filter = ('timestamp',)                            # Enable filtering by specific fields
    ordering = ('-timestamp',)                              # Default ordering (newest first)
    readonly_fields = ('contact', 'message', 'timestamp')  # Make specific fields read-only

    fieldsets = (
        (None, {
            'fields': ('contact', 'message')
        }),
        ('Timestamps', {
            'fields': ('timestamp',),
        }),
    )
