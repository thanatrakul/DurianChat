from apps.fb_pages.models import FacebookPage
from django.db import models
from django.utils.timezone import now


class Contact(models.Model):
    page = models.ForeignKey(FacebookPage, on_delete=models.CASCADE, related_name='contacts')  # เชื่อมกับ Facebook Page
    name = models.CharField(max_length=100)  # ชื่อของผู้ติดต่อ
    user_id = models.CharField(max_length=255, unique=True)  # User ID ในระบบ Facebook Messenger (unique)
    profile_picture = models.URLField(max_length=500, null=True, blank=True)  # รูปโปรไฟล์ (URL)
    last_message = models.TextField(null=True, blank=True)  # ข้อความล่าสุด
    last_contacted = models.DateTimeField(default=now)  # วันที่ติดต่อครั้งล่าสุด
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่สร้างข้อมูลนี้
    updated_at = models.DateTimeField(auto_now=True)  # วันที่อัปเดตข้อมูลครั้งล่าสุด

    def __str__(self):
        return f"{self.name} ({self.page.name})"
