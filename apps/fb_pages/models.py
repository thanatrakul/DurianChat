from django.db import models


class FacebookPage(models.Model):
    page_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='page_icons/')
    access_token = models.TextField()  # เก็บ Access Token
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
