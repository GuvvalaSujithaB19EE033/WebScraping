from django.db import models

class Candidate(models.Model):
    Title = models.CharField(max_length=255)
    Company = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Salary = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.Title  # Display the Title in the admin interface