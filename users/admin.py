from django.contrib import admin

from users.models.agent import Agent
from users.models.leads import Lead
from users.models.meetings import Meeting
from users.models.lead_history import LeadHistory

# Register your models here.
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(Meeting)
admin.site.register(LeadHistory)