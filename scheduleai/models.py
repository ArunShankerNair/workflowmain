from django.db import models

# Create your models here.

class WorkToDo(models.Model):
    user=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    category=(
        ("household_works","household_works")
        ("office_works","office_works")
        ("miscellaneous_works","miscellaneous_works")
        
    )
    workupdate=(
        ("completed","completed")
        ("pending","pending")
    )
    options=models.CharField(max_length=200,choices=category,default="miscellaneous")
    status=models.CharField(max_length=200,choices=workupdate,default="pending")

    def __str__(self):
        return self.title
