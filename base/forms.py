from django import forms
from django.db.models import fields
from django.forms import ModelForm, DateInput, widgets
from django.db.models.fields import DateField, TextField, IntegerField
from datetime import date, datetime, timezone
from django.contrib.auth.models import User
from . import models
    

class EventForm(ModelForm):
  class Meta:
    model = models.Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      # 'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y'),
      # 'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y'),
      'start_date': DateInput(attrs={'type': 'date'}, format='%m-%d-%Y'),
      'end_date': DateInput(attrs={'type': 'date'}, format='%m-%d-%Y'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_date'].input_formats = ('%m-%d-%Y',)
    self.fields['end_date'].input_formats = ('%m-%d-%Y',)
