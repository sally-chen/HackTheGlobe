from django.shortcuts import render
from django.http import HttpResponse

from .models import Services, Categories
from django.template import loader

def index(request):
    services_list = Services.objects.all()
    template = loader.get_template('events_and_services/index.html')
    print(services_list)
    print(services_list[0].category.all())
    context = {
        'service_list': services_list,
    }
    return HttpResponse(template.render(context, request))