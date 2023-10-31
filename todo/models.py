from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Task(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)
    
    def __str__(self):
        return str(self.title)
    

