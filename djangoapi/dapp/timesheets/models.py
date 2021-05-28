from django.db import models


class Timesheet(models.Model):
    project = models.CharField(max_length=100)
    task = models.CharField(max_length=300)
    hours = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.project} : {self.task} : {self.hours}"
