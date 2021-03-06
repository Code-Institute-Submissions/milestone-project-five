from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Feature(models.Model):
    
    
    feature_title = models.CharField(max_length=200, blank=False)
    feature_author = models.ForeignKey(User)
    details = models.TextField(blank=False)
    purchased = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.feature_title
        
