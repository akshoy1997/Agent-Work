from users.api.base import BaseModelViewSet
from users.api.base import BaseSerializer

from users.models.agent import Agent

class AgentSerializer(BaseSerializer):
    class Meta:
        model = Agent
        fields = (
            'id',
            'username',
            'password',
            'email',
            'phone_number',
            'is_staff',
            'is_superuser'
        )
        read_only_fields = ['is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Override create to hash the password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # Override create to hash the password
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class AgentViewSet(BaseModelViewSet):
    """
    URL: http://localhost:8000/api/user/1/
         http://localhost:8000/api/user/
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer