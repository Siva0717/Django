from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
     name=models.CharField(max_length=200)

     def __str__(self):
          return self.name



class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.name)
    



    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE)
        room=models.ForeignKey(Room, on_delete=models.CASCADE)    #on_delete=models.SET_NULL
        body=models.TextField()
        
        def __str__(self):
            return self.body[0:50]
        
class Student(models.Model):
     sno=models.IntegerField()
     sname=models.CharField(max_length=100)
     sclass=models.IntegerField()
     saddress=models.CharField(max_length=100)

     def __str__(self):
          return self.sname
        
class school(models.Model):
     person=models.CharField(max_length=100)
     Age=models.IntegerField()
     def __str__(self):
          return self.sname
     
class shop(models.Model):
     department=models.CharField(max_length=20)
     stock=models.IntegerField()
     customer=models.IntegerField()
     
     def __str__(self):
          return self.department



# Create your models here.
class college(models.Model):
     students=models.CharField(max_length=100)
     teachers=models.CharField(max_length=100)
     marks=models.IntegerField()

    
     def __str__(self):
       return self.students
 










     
class hotel(models.Model):
    

     tables=models.IntegerField()
     password=models.CharField(max_length=100)

class university(models.Model):
     seats=models.IntegerField()
     name=models.CharField(max_length=20)
     course=models.IntegerField(max_length=30)

class inventory(models.Model):
     name=models.CharField(max_length=20)
     age=models.IntegerField()
     department=models.CharField(max_length=20)
    
     
    
     