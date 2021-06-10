from django.db import models

class SingleDayRequest(models.Model):
    submition_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    availability = models.BooleanField()
    shift = models.CharField(max_length=10)
    note = models.CharField(max_length=300)
    name = models.CharField(max_length=50)


class DurationRequest(models.Model):
    submition_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=50)
