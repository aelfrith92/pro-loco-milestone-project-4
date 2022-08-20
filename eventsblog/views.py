from django.shortcuts import render, get_object_or_404
from  django.views import generic, View
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("scheduled_on")
    template_name = "index.html"
    paginate_by = 6


class EventOverview(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by('-created_on')
        # The following 2 lines will prove useful both when liking/disliking
        # and for front-end purposes
        joined = False
        # if event.joins.filter(id=self.request.user.id).exists():
        #     joined = True

        return render(
            request,
            "event_overview.html",
            {
                "event": event,
                "comments": comments,
                "joined": joined,
            }
        )
