from django.db import models
from departments.models import Department
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    joined_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
