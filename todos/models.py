from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    idade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)