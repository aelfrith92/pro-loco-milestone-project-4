from django.urls import path
from . import views

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path('suggestE/', views.Suggestion.as_view(), name='suggestion'),
    path('<slug:slug>/', views.EventOverview.as_view(), name='event_detail'),
    path('join/<slug:slug>', views.EventJoin.as_view(), name='event_join'),
    path('update/<slug:slug>', views.UpdateEvent.as_view(), name='update'),
    path('delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete'),
]
