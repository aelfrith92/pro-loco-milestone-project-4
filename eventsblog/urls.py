from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path('suggestE/', views.Suggestion.as_view(), name='suggestion'),
    path('<slug:slug>/', views.EventOverview.as_view(), name='event_detail'),
    path('join/<slug:slug>', views.EventJoin.as_view(), name='event_like'),
    path('update/<slug:slug>', views.UpdateEvent.as_view(), name='update'),
]
