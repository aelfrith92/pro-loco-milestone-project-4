from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'scheduled_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'scheduled_on')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['cancel_event', 'schedule_event']

    def cancel_event(self, request, queryset):
        queryset.update(status=2)
 
    def schedule_event(self, request, queryset):
        queryset.update(status=1)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'event', 'created_on', 'approved', 'audience')
    list_filter = ('approved', 'created_on', 'audience')
    search_fields = ('name', 'email', 'body', 'audience')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
