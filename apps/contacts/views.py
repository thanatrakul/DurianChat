from .models import Contact
from apps.fb_pages.models import FacebookPage
from django.views.generic import DetailView
from django.views.generic import ListView


class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contacts.html'
    context_object_name = 'contacts'
    extra_context = {
        'active_menu': 'contacts',
        'fb_page': FacebookPage.objects.filter(is_active=True).first()
    }

    def get_queryset(self):
        # ดึงเฉพาะ Contacts ของ Facebook Page ที่เลือก
        page = FacebookPage.objects.filter(is_active=True).first()
        if page:
            return Contact.objects.filter(page=page).order_by('-last_contacted')
        return Contact.objects.none()  # กรณีไม่มี Page ที่เลือก


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contact'
    extra_context = {
        'active_menu': 'contacts',
        'fb_page': FacebookPage.objects.filter(is_active=True).first()
    }
