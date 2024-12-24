from .views import ActivatePageView
from .views import AddNewPageView
from .views import FacebookHomeView
from django.urls import path

app_name = "facebook_managments"

urlpatterns = [
    path("", FacebookHomeView.as_view(), name="home"),  # หน้า Home
    path("add/", AddNewPageView.as_view(), name="add_page"),
    path("activate/<int:pk>/", ActivatePageView.as_view(), name="activate_page"),  # เปลี่ยน Active Page
]
