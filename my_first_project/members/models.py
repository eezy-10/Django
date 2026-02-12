from django.db import models

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

# Approach 1
# Essential as it is used to display the objects as these names in the admin panel
    def __str__(self):
        return f"{self.firstName} {self.lastName}"