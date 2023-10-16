from django.db import models

# Create your models here.

class XUsers(models.Model):
    Username = models.TextField(max_length=40)
    Password = models.TextField(max_length=60)
    Type = models.BooleanField()

class Emplooyes(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.TextField(default='None',null=True)
    Mobile = models.IntegerField(default=10,null=True)
    Address = models.TextField(default='None',null=True)
    Email = models.TextField(default='None',null=True)
    Birthdate = models.DateField(null=True)
    Salary = models.IntegerField(default=1000,null=True)
    Department = models.TextField(default='Genral',null=True)
    Gender = models.TextField(default='Male',null=True)
    Mstatue = models.TextField(default='Single',null=True)
    AviVacdays = models.IntegerField(default=5,null=True)

    
class HRs(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.TextField(default='None',null=True)
    Password = models.TextField(default='None',null=True)
    Mobile = models.IntegerField(default=10,null=True)
    Address = models.TextField(default='None',null=True)
    Email = models.TextField(default='None',null=True)
    Birthdate = models.DateField(null=True)
    Salary = models.IntegerField(default=1000,null=True)
    Department = models.TextField(default='HR',null=True)
    Gender = models.TextField(default='Male',null=True)
    Mstatue = models.TextField(default='Single',null=True)
    AviVacdays = models.IntegerField(default=5,null=True)


class Vactions(models.Model):
    EmployeeUsername = models.TextField(default='none',null=False)
    EmployeeDepartment = models.TextField(default='none',null=False)
    Startdate = models.DateField(null=True)
    Enddate = models.DateField(null=True)
    Reason = models.TextField(null=True,default='Personal Reasons')
    Statues = models.TextField(default='Panding')

