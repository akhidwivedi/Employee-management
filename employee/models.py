from django.db import models
from django.forms import ModelForm

# Create your models her
class position(models.Model):
    title=models.CharField(max_length=40)
    def __str__(self):
        return self.title



class employee(models.Model):
    fullname=models.CharField(max_length=50)
    emp_code=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30)
    position=models.ForeignKey(position,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname









     



