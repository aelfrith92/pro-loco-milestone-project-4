from django.shortcuts import render, get_object_or_404, reverse, get_list_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Event
from django.contrib import messages
from django.utils.text import slugify
from .forms import CommentEventForm, SuggestEventForm


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
        if event.joins.filter(id=self.request.user.id).exists():
            joined = True

        return render(
            request,
            "event_overview.html",
            {
                "event": event,
                "comments": comments,
                "joined": joined,
                "comment_form": CommentEventForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        joined = False
        if event.joins.filter(id=self.request.user.id).exists():
            joined = True

        comment_form = CommentEventForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            if request.user.is_staff:
                comment_form.instance.approved = True
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
        else:
            comment_form = CommentEventForm()

        return render(
            request,
            "event_overview.html",
            {
                "event": event,
                "comments": comments,
                "commented": True,
                "joined": joined,
                "comment_form": CommentEventForm(),
            },
        )


class EventJoin(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        if event.joins.filter(id=request.user.id).exists():
            event.joins.remove(request.user)
        else:
            event.joins.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class Suggestion(CreateView):

    model = Event
    form_class = SuggestEventForm
    template_name = "suggestion.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        form.instance.email = self.request.user.email
        form.instance.author_id = self.request.user.id
        form.instance.slug = slugify(form.instance.title)
        suggested_date = form.instance.scheduled_on
        # Checking whether the chosen date is already taken
        scheduled_events = Event.objects.values_list('scheduled_on')
        for day in scheduled_events.values('scheduled_on'):
            if day['scheduled_on'].strftime("%x") == suggested_date.strftime("%x"):
                messages.warning(
                    self.request, 'The chosen date is taken by'
                    ' another event. See the homepage for the available dates.'
                )
                return HttpResponseRedirect(reverse('suggestion', ))
        messages.success(
            self.request, 'Event successfully submitted for '
            'review'
        )
        return super(Suggestion, self).form_valid(form)
