from django.db import models
from django.contrib.auth.models import User

# Model representing a bus
class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=50)
    bus_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.bus_name} ({self.bus_number})"

    class Meta:
        db_table = "bus"

# Model representing a passenger
class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger_profile')
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=225, default='default@example.com')
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "passenger"

# Model representing a pass
class Pass(models.Model):
    pass_id = models.AutoField(primary_key=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='passes')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='passes')

    def __str__(self):
        return f"{self.passenger.name} - {self.bus.bus_name} ({self.bus.bus_number})"

    class Meta:
        db_table = "pass"
