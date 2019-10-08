from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    employees = models.CharField(max_length=128, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class Interactions(models.Model):
    action_choices = (
        ('ta', 'Task'),
        ('ev', 'Event'),
        ('co', 'Call'),
    )

    action = models.CharField(max_length=5, choices=action_choices)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.name = models.ForeignKey(Contacts, related_name='interactions', on_delete=models.CASCADE)
