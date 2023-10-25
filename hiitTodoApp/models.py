from django.db import models
from django.contrib.auth.models import User

PRIORITIES = (('L', 'Low'), ('M', 'Mid'), ('H', 'High'))

class Category(models.Model):
    title = models.CharField(max_length= 255)

    def __str__(self) -> str:
        return self.title
    
class hiitTodo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now= True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    priority = models.CharField(choices= PRIORITIES, max_length=50, null=True) 


    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    todo = models.ForeignKey(hiitTodo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment