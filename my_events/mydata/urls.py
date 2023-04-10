from django.urls import path
from . import views

app_name = 'mydata'

urlpatterns = [
    path('', views.index, name='mydata'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/update', views.event_update, name='event_update'),
    path("create", views.event_create, name="event_create"),
]

