from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    icon = models.ImageField(upload_to='icons', null=True, blank=True)
    icon_blurhash = models.TextField(null=True, blank=True)
    real_name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
