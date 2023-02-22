from django.db import models

# Create your models here.

class Job(models.Model):
    job_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.job_name

class Person(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job", null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
