# campaigns/admin.py
from django.contrib import admin
from .models import Campaign, CampaignLead

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'start_date')
    list_filter = ('status', 'channels')
    search_fields = ('name', 'owner__email')

@admin.register(CampaignLead)
class CampaignLeadAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'lead_email', 'response_status')
    list_filter = ('response_status', 'campaign')
    
