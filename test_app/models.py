from django.db import models

# Create your models here.
    
class Student(models.Model):
    name = models.TextField(max_length=200)
    degree = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
# class Company(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=200)

# class Job(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)  
      
# class CompanyProfile(models.Model):
#     company = models.OneToOneField(Company, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)    



# class Person(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=200)
    
# class App(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=200)    

# class PersonProfile(models.Model):
#     company = models.OneToOneField(Company, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)  