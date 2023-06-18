from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
