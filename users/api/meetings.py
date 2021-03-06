from users.api.base import BaseModelViewSet, BaseSerializer
from users.models.meetings import Meeting


class MeetingSerializer(BaseSerializer):
    class Meta:
        model = Meeting
        fields = (
            'id',
            'lead',
            'type',
            'date',
            'time',
            'status',
            'details',
            'follow_up_date',
            'latitude',
            'longitude',
        )


class MeetingViewSet(BaseModelViewSet):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        """
        This view should return a list of all the leads
        for the currently authenticated user.
        """
        queryset = Meeting.objects.all()
        lead_id = self.request.query_params.get('lead_id', None)
        if lead_id is not None:
            queryset = queryset.filter(lead=lead_id)
        return queryset
