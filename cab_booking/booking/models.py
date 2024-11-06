# from django.db import models

# Create your models here.
from django.db import models

class Cab(models.Model):
    driver_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.driver_name} - {self.location}"

class Ride(models.Model):
    customer_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride for {self.customer_name} from {self.pickup_location} to {self.dropoff_location}"
