from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_applied = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company}"