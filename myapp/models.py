from django.db import models

class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=50)
    bus_number = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "bus"

class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=100)
    email = models.EmailField(max_length = 225, default = 'default@example.com')
    contact = models.CharField(max_length = 15)

    class Meta:
        db_table = "passenger"

class Pass(models.Model):
    pass_id = models.AutoField(primary_key=True)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "pass"