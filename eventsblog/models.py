from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

STATUS = ((0, "Draft"), (1, "Published"), (2, "Cancelled"))
AUDIENCE = ((0, "Admin"), (1, "Everyone"))

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_events"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    txt_preview = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    joins = models.ManyToManyField(
        User, related_name='blogevent_like', blank=True)
    scheduled_on = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ["scheduled_on"]

    def __str__(self):
        return self.title

    def number_of_joins(self):
        return self.joins.count()


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="events")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    audience = models.IntegerField(choices=AUDIENCE, default=1)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
