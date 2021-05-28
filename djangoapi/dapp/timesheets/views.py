from django.shortcuts import render
from rest_framework import viewsets
from .models import Timesheet
from .serializers import TimesheetSerializer


class TimesheetView(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer
