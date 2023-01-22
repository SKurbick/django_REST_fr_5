from django.db import models
from django.forms.fields import ImageField


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    image = ImageField(allow_empty_file=True)
