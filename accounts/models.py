from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
        
        
class Address(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
     full_name = models.CharField(max_length=120)
     phone = models.CharField(max_length=20)
     line1 = models.CharField(max_length=255)
     line2 = models.CharField(max_length=255, blank=True)
     city = models.CharField(max_length=100)
     district = models.CharField(max_length=100)
     upozilla = models.CharField(max_length=100)

     postal_code = models.CharField(max_length=20)
     is_default = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True)


class Meta:
 ordering = ["-is_default", "-created_at"]


def __str__(self):
 return f"{self.full_name} — {self.line1}, {self.city}"   