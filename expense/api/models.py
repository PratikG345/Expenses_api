from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
class Expense(models.Model):
    amount = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    essential = models.BooleanField()
    
    def __str__(self):
        return f"{self.category}-{self.amount}-{self.date}"
    
