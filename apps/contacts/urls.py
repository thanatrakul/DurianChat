from .views import ContactDetailView
from .views import ContactListView
from django.urls import path

app_name = 'contacts'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
