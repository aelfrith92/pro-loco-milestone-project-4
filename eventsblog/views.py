from django.shortcuts import render
from  django.views import generic
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("scheduled_on")
    template_name = "index.html"
    paginate_by = 6
