# campaigns/urls.py
from django.urls import include, path
from .views import CampaignListCreateAPI, CampaignDetailAPI

urlpatterns = [
    path('', CampaignListCreateAPI.as_view()),
    path('<int:pk>/', CampaignDetailAPI.as_view()),
]

# core/urls.py (update)
urlpatterns = [
    # ... existing paths ...
    path('api/campaigns/', include('campaigns.urls')),
]