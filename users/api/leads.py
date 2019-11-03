from users.api.base import BaseModelViewSet, BaseSerializer
from users.models.leads import Lead
from rest_framework.response import Response
from rest_framework import generics

class LeadSerializer(BaseSerializer):
    class Meta:
        model = Lead
        fields = (
            'id',
            'agent',
            'name',
            'phone_number',
            'address',
            'status',
        )


class LeadViewSet(BaseModelViewSet):

    serializer_class = LeadSerializer

    def get_queryset(self):
        """
        This view should return a list of all the leads
        for the currently authenticated user.
        """
        user = self.request.user
        return Lead.objects.filter(agent=user)

    def partial_update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        lead = Lead.objects.get(id=pk)
        lead.status = request.data['status']
        lead.save()
        return Response({'message': 'Partially Updated'})

        
    
    