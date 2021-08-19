from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=200)
    job_description=models.TextField()
    email=models.EmailField()
    date=models.DateTimeField(auto_now_add=True)