from rest_framework import serializers
from .models import Community, Event

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'  # Serialize all fields

class EventSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(read_only=True)  # Nested community details
    community_id = serializers.PrimaryKeyRelatedField(
        queryset=Community.objects.all(), write_only=True, source="community"
    )  # Allow setting community by ID

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'speakers', 'date', 'links', 'community', 'community_id', 'organizers', 'created_at']
