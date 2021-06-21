from django.db import models

class ScheduleRequest(models.Model):
    submition_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    availability = models.CharField(max_length=10)
    note = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        if self.note != '':
            return '{} - {} - {} | {}'.format(
                self.date.strftime("%m/%d/%y"),
                self.name.title(),
                self.availability.title(),
                self.note.capitalize()
            )
        return '{} - {} - {}'.format(
            self.date.strftime("%m/%d/%y"),
            self.name.title(),
            self.availability.title(),
        )
