from django.db import models
from django.contrib.auth.models import User  

class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    channels = models.CharField(max_length=255, blank=True)  
    total_members = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    speakers = models.CharField(max_length=255, blank=True)  
    date = models.DateTimeField()
    links = models.URLField(max_length=500, blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='events')
    organizers = models.ManyToManyField(User, related_name='organized_events')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
