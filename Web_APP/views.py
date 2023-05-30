from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
import joblib
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        home = ContactUS(name=name, number=number, subject=subject, message=message,) 

        home.save()
        messages.success(request, 'Your form has been submitted!')
    return render(request, 'Web_App/index.html')

def crops(request):
    return render(request, 'Web_App/crops.html')

def disease(request):
    return render(request, 'Web_App/disease.html')



def crop_result(request):

    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['NITROGEN'])
    lis.append(request.GET['PHOSPHORUS'])
    lis.append(request.GET['POTASSIUM'])
    lis.append(request.GET['TEMPERATURE'])
    lis.append(request.GET['HUMIDITY'])
    lis.append(request.GET['PH'])
    lis.append(request.GET['RAINFALL'])

    ans = cls.predict([lis])


    return render(request, 'Web_App/crop_result.html', {'ans':ans})

class WheatDView(ListView):
    model = Wheat_Disease
class WheatView(DetailView):
    model = Wheat_Disease


class RiceDView(ListView):
    model = Rice_Disease
class RiceView(DetailView):
    model = Rice_Disease


class PotatoDView(ListView):
    model = Potato_Disease
class PotatoView(DetailView):
    model = Potato_Disease


class GroundnutDView(ListView):
    model = Groundnut_Disease
class GroundnutView(DetailView):
    model = Groundnut_Disease


class PulsesDView(ListView):
    model = Pulses_Disease
class PulsesView(DetailView):
    model = Pulses_Disease


class TomatoDView(ListView):
    model = Tomato_Disease
class TomatoView(DetailView):
    model = Tomato_Disease