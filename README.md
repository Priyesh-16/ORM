# Ex02 Django ORM Web Application
## Date: 23/04/2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![ER](<ER DIAGRAM (2).png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie,UserID
admin.site.register(Movie,UserID)

models.py

from django.db import models
from django.contrib import admin
class Movie (models.Model):
    User_id=models.IntegerField(primary_key=True)
    User_name=models.CharField(max_length=100)
    email=models.EmailField()
    Movie_name=models.CharField(max_length=100)
    No_of_seats=models.IntegerField()
    
 
class UserID(admin.ModelAdmin):
    list_display=('User_id','User_name','email','Movie_name','No_of_seats')

# Create your models here.
```



## OUTPUT

Include the screenshot of your admin page.

![alt text](<Screenshot 2025-04-23 212955.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
