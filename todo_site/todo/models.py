from django.db import models
from django.utils import timezone

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    user_id=models.IntegerField()

    def __str__(self):
        return self.name

class Todo(models.Model):
    title=models.CharField(max_length=50)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title