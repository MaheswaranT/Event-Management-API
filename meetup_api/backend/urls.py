from django.urls import path
from .views import CommunityListCreateView, CommunityDetailView, EventListCreateView, EventDetailView
from .views import EventCreateView

urlpatterns = [
    # Community URLs
    path('communities/', CommunityListCreateView.as_view(), name='community-list-create'),
    path('communities/<int:pk>/', CommunityDetailView.as_view(), name='community-detail'),

    # Event URLs
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/create/', EventCreateView.as_view(), name='create-event'),
]
