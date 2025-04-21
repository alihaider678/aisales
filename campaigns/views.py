from django.shortcuts import render

# campaigns/views.py
from rest_framework import generics, permissions
from .models import Campaign
from .serializers import CampaignSerializer

class CampaignListCreateAPI(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CampaignDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]
