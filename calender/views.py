import calendar
from django.shortcuts import get_object_or_404, redirect, render
from.models import Events
from.forms import CalenderRegistrationForm
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from.models import *
from.utils import Calendar
from datetime import date
from datetime import datetime, timedelta
from django.http.response import HttpResponseRedirect
from django.shortcuts import render ,redirect

class CalendarView(generic.ListView):
    model = Events
    template_name = 'calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))
        calendar = Calendar(d.year, d.month)
        html_cal = calendar.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
       

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date (year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Events()
    if event_id:
        instance = get_object_or_404(Events, pk=event_id)
    else:
        instance = Events()
    
    form = CalenderRegistrationForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'events.html', {'form': form})

def register_calender(request):
    if request.method=="POST":
        form=CalenderRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect (register_calender)
        else:
            print(form.errors)
    else:
        form=CalenderRegistrationForm()
    return render(request,"register_calender.html",{"form":form})
def calendar_profile(request,id):
    calendar=Events.objects.get(id=id)
    return render(request,"calender_profile.html",{"calendar":calendar})

def edit_calender(request,id):
    calendar=Events.objects.get(id=id)
    if request.method=="POST":
        form=CalenderRegistrationForm(request.Post,instance=calendar)
        if form.is_valid():
            form.save    
            return  redirect("calender_profile",id=calendar.id)
    else:
        form=CalenderRegistrationForm(instance=calendar) 
        return render(request,"edit_calender.html",{"form":form})      

