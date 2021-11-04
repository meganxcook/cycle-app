from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.utils.safestring import mark_safe

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime, timedelta, date

import calendar
from .models import *
from .models import Event, Profile
from .utils import Calendar
from .forms import EventForm


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile-create')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['first_name', 'lmp', 'typical_flow_length', 'typical_cycle_length', 'typical_symptoms', 'current_bc_method', 'goal']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)

# hui wen calendar tutorial
class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
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
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event-create.html', {'form': form})
# ----------

def view_events(request):
    all_events = Event.objects.all()
    return render(request, 'event-list.html', {'all_events': all_events})

# class EventList(LoginRequiredMixin, ListView):
#     model = Event
#     context_object_name = 'events'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['events'] = context['events'].filter(user=self.request.user)
#         return context

# class EventDetail(LoginRequiredMixin, DetailView):
#     model = Event
#     context_object_name = 'event'
#     template_name = 'base/event.html'

# class EventCreate(LoginRequiredMixin, CreateView):
#     model = Event
#     fields = ['title', 'period_started', 'period_ended', 'symptoms', 'mood', 'cramps', 'flow', 'libido', 'sperm', 'result', 'bbt', 'lh', 'notes']
#     success_url = reverse_lazy('calendar')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(EventCreate, self).form_valid(form)

# class EventUpdate(LoginRequiredMixin, UpdateView):
#     model = Event
#     fields = ['title', 'period_started', 'period_ended', 'symptoms', 'mood', 'cramps', 'flow', 'libido', 'sperm', 'result', 'bbt', 'lh', 'notes']
#     success_url = reverse_lazy('calendar')

# class DeleteView(LoginRequiredMixin, DeleteView):
#     model = Event
#     context_object_name = 'event'
#     success_url = reverse_lazy('calendar')

# @login
def home(request):
    return render(request, 'base/home.html')

# @login
def profile_view(request):
    return render(request, 'base/profile.html')

# @login
def snapshot(request):
    return render(request, 'base/snapshot.html')

def about(request):
    return render(request, 'base/about.html')