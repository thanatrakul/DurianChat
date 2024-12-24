from apps.fb_pages.models import FacebookPage
from django.views.generic import TemplateView


class ShareContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fb_page'] = FacebookPage.objects.filter(is_active=True).first()
        return context


class HomeView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fb_page'] = FacebookPage.objects.filter(is_active=True).first()
        context['active_menu'] = "home"
        return context


class AutomationView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'active_menu': 'automation'}


class BroadcastingView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'active_menu': 'broadcasting'}


class AdsView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'active_menu': 'ads'}


class SettingsView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'active_menu': 'settings'}


class ProfileView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'active_menu': 'profile'}


class HelpView(ShareContextMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'active_menu': 'help'}
