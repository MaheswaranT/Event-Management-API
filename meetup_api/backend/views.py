from rest_framework import generics, permissions, filters
from .models import Community, Event
from .serializers import CommunitySerializer, EventSerializer
from django.utils.timezone import now

# List and Create Community
class CommunityListCreateView(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.AllowAny]  # Open access

# Retrieve, Update, Delete Community
class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

# List and Create Events
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]  # Open access for now
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']  # Allow sorting by date

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.query_params.get('filter', None)

        if filter_type == "past":
            return queryset.filter(date__lt=now())  # Past events
        elif filter_type == "future":
            return queryset.filter(date__gte=now())  # Future events

        return queryset  # Return all events by default

# Retrieve, Update, Delete Event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users
