from django.db import models
from django.contrib.auth.models import User  

class Community(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    channels = models.JSONField(default=list)  # Ensures valid JSON always
    created_at = models.DateTimeField(auto_now_add=True)
    total_members = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    speakers = models.JSONField(default=list)  # Default as empty list
    organizers = models.JSONField(default=list)
    date = models.DateTimeField()
    links = models.JSONField(default=list)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="events")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name