from .forms import FacebookPageForm
from .models import FacebookPage
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class FacebookMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Active Page
        context['active_menu'] = "fb_pages"
        context["fb_page"] = FacebookPage.objects.filter(is_active=True).first()

        return context


class FacebookHomeView(FacebookMixin, TemplateView):
    """
    แสดงหน้า Facebook Page Management
    """
    template_name = "fb_pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Active Page: ดึง Page ที่ถูก Active
        context["active_page"] = FacebookPage.objects.filter(is_active=True).first()

        # List of Pages: ดึงรายการ Pages ทั้งหมด
        context["pages"] = FacebookPage.objects.order_by('pk')

        return context


class ActivatePageView(RedirectView):
    pattern_name = "fb_pages:home"

    def get_redirect_url(self, *args, **kwargs):
        page_id = kwargs.get("pk")
        page = get_object_or_404(FacebookPage, pk=page_id)

        # Reset all Pages to not active
        FacebookPage.objects.update(is_active=False)

        # Set the selected page as active
        page.is_active = True
        page.save()

        # Redirect to "home" without kwargs
        return reverse_lazy("fb_pages:home")


class AddNewPageView(CreateView):
    model = FacebookPage
    form_class = FacebookPageForm  # ใช้ฟอร์มที่กำหนดเอง
    template_name = "fb_pages/add_page.html"
    success_url = reverse_lazy("fb_pages:home")
