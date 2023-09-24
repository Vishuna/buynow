from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.


class Role(models.Model):
    role_id=models.IntegerField()
    role_name=models.CharField(max_length=50)

    def __str__(self):
        return str(self.role_id)
    
class Register(models.Model):
    first_name=models.CharField(max_length=30,blank=True,null=True)
    last_name=models.CharField(max_length=30,blank=True,null=True)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    role=models.ForeignKey(Role,default=1,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    last_login=models.DateTimeField(auto_now=True)

    

class CustomGroup(models.Model):
    g_id=models.IntegerField()
    groups= models.ForeignKey(Group,on_delete=models.CASCADE)



    





