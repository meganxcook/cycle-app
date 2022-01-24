from django.contrib import admin
from .models import Profile, Event, PeriodEvent, SymptomEvent, SpermEvent, FertilityEvent, LibidoEvent, MoodEvent, EnergyEvent

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(PeriodEvent)
admin.site.register(SymptomEvent)
admin.site.register(SpermEvent)
admin.site.register(FertilityEvent)
admin.site.register(LibidoEvent)
admin.site.register(MoodEvent)
admin.site.register(EnergyEvent)
