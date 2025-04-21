from django.db import models
from accounts.models import User

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('PAUSED', 'Paused'),
        ('COMPLETED', 'Completed'),
    ]
    
    CHANNEL_CHOICES = [
        ('LINKEDIN', 'LinkedIn'),
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    channels = models.JSONField(default=list)  # Stores selected channels e.g. ['LINKEDIN', 'EMAIL']
    target_industries = models.JSONField(default=list)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    message_templates = models.JSONField(default=dict)  # {channel: template_text}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

class CampaignLead(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    lead_email = models.EmailField()
    last_contacted = models.DateTimeField(null=True, blank=True)
    response_status = models.CharField(max_length=50, default='NOT_CONTACTED')
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('campaign', 'lead_email')