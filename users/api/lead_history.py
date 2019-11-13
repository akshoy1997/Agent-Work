from users.api.base import BaseModelViewSet, BaseSerializer
from users.models.lead_history import LeadHistory


class LeadHistorySerializer(BaseSerializer):
    class Meta:
        model = LeadHistory
        fields = (
            'id',
            'lead',
            'status',
            'registered_phone_nos',
            'more_details',
            'reason',
            'detailed_reason'
        )


class LeadHistoryViewSet(BaseModelViewSet):
    serializer_class = LeadHistorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the leads
        for the currently authenticated user.
        """
        queryset = LeadHistory.objects.all()
        lead_id = self.request.query_params.get('lead_id', None)
        if lead_id is not None:
            queryset = queryset.filter(lead=lead_id)
        return queryset
