from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path('<slug:slug>/', views.EventOverview.as_view(), name='event_detail'),
    path('join/<slug:slug>', views.EventJoin.as_view(), name='event_like')
]
