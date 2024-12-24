# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from apps.home.views import (
    HomeView, AutomationView, BroadcastingView, AdsView, SettingsView, ProfileView, HelpView
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    path('', HomeView.as_view(), name='home'),
    path('automation/', AutomationView.as_view(), name='automation'),
    path('broadcasting/', BroadcastingView.as_view(), name='broadcasting'),
    path('ads/', AdsView.as_view(), name='ads'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('help/', HelpView.as_view(), name='help'),

    # Page Management
    path("facebook-managements/", include("apps.fb_pages.urls", namespace="fb_pages")),

    # Contacts
    path("contacts/", include("apps.contacts.urls", namespace="contacts")),

    # Conversations
    path("conversations/", include("apps.fb_conversations.urls", namespace="fb_conversations")),

    # Webhooks
    path("webhooks/", include("apps.webhooks.urls", namespace="webhooks")),

    # Live Chats
    path("live-chats/", include("apps.live_chats.urls", namespace="live_chats")),

    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # User management
    path("users/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),

    # Your stuff: custom urls includes go here
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
