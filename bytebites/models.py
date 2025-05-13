from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.EmailField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    height = models.FloatField()
    weight = models.FloatField()
    is_veg = models.BooleanField()

    def __str__(self):
        return (f"{self.first_name} {self.last_name}'s profile")
    
    def calculate_bmi(self):
        height_m = self.height / 100
        return round(self.weight / (height_m ** 2), 2)