# campaigns/serializers.py
from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
        read_only_fields = ('owner', 'created_at', 'updated_at')

    def validate(self, data):
        # Custom validation logic here
        if data['start_date'] > data.get('end_date', data['start_date']):
            raise serializers.ValidationError("End date must be after start date")
        return data