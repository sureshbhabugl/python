from rest_framework import serializers
from .models import Timesheet


class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        field = ('id', 'project', 'task', 'hours')
