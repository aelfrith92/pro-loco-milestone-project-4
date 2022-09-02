from django.contrib import admin
from .models import Event, Comment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    '''This class defines forms and related actions/tools in the admin area
    Event management'''
    list_display = ('title', 'slug', 'status', 'created_on', 'scheduled_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'scheduled_on')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['cancel_event', 'schedule_event']

    def cancel_event(self, request, queryset):
        '''Adds the function Cancel Event to possible actions in
        the admin area'''
        queryset.update(status=2)

    def schedule_event(self, request, queryset):
        '''Adds the function Schedule Event to possible actions in
        the admin area'''
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''This class defines forms and related actions/tools in the admin area
    Comment management'''
    list_display = ('name', 'body', 'event', 'created_on', 'approved',
                    'audience')
    list_filter = ('approved', 'created_on', 'audience')
    search_fields = ('name', 'email', 'body', 'audience')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        '''Adds the function Approve Comment to possible actions in
        the admin area'''
        queryset.update(approved=True)
