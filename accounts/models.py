from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    target_market = models.CharField(max_length=50, choices=[
        ('SMB', 'Small Business'),
        ('MID', 'Mid Market'),
        ('ENT', 'Enterprise')
    ])

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('ADMIN', 'Admin'),
        ('SALES', 'Sales Rep'),
        ('MANAGER', 'Manager')
    ])
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    onboarding_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} ({self.role})"