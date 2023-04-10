from django.shortcuts import render
from django.http import HttpResponse
from mydata.models import Event
# Create your views here.

def index(request):

    data = {
        "events": Event.objects.all()
    }

    #add template name here
    return render(request, "mydata/index.html", data)

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    if not event:
        HttpResponse("Event not found or doesn't exist")
    data = {
        "my_event": event
    }

    return render(request, "mydata/detail.html", data)

def event_create(request):
   # update_event = Event.objects.get(pk=event_id)

    if request.method == "POST":
        try:
            new_event = Event()
            new_event.name = request.POST['name']
            new_event.description = request.POST['description']
            #if new_event.full_clean():
            new_event.save()
            return HttpResponse("New Event created!!")
            return HttpResponse("Something went wrong while creating event")
        except:
            return HttpResponse("Error creating new event")
        

    data = {
            "update_event": None,
            "create_or_update": True
        }
    
    return render(request, "mydata/form.html")

def event_update(request, event_id):
    update_event = Event.objects.get(pk=event_id)

    if request.method == "POST":
        try:
            update_event.name = request.POST['name']
            update_event.description = request.POST['description']
            #if new_event.full_clean():

            update_event.save()
            return HttpResponse("New Event created!!")
        except:
            return HttpResponse("Error creating new event")
        

    data = {
            "update_event": update_event,
            "create_or_update": False
        }
    
    return render(request, "mydata/form.html")

def event_form():
    pass