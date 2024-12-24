from apps.contacts.models import Contact
from django.db import models
from django.utils.timezone import now


class Conversation(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='conversations')
    message = models.TextField()  # ข้อความ
    direction = models.CharField(max_length=10, choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')])  # ทิศทางข้อความ
    is_read = models.BooleanField(default=False)  # สถานะการอ่าน
    timestamp = models.DateTimeField(default=now)  # เวลาที่ส่งข้อความ

    def __str__(self):
        return f"Message to/from {self.contact.name}"
