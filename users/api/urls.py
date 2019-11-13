from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from users.api.agent import AgentViewSet
from users.api.leads import LeadViewSet
from users.api.meetings import MeetingViewSet
from users.api.lead_history import LeadHistoryViewSet

"""
If unset the basename will be automatically generated based on the queryset attribute of the viewset, 
if it has one. Note that if the viewset does not include a queryset 
attribute then you must set basename when registering the viewset.
"""
router = routers.DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'leads', LeadViewSet, basename='leads')
router.register(r'meetings', MeetingViewSet, basename='meetings')
router.register(r'lead_history',LeadHistoryViewSet, basename='lead_history')

urlpatterns = [
    url(r'^', include(router.urls)),
]
