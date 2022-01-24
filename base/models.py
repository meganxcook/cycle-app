from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import date, timedelta


class Profile(models.Model):
    SYMPTOMS = (
        ('NONE', 'None'),
        ('HEADACHE', 'Headaches'),
        ('MIGRAINE', 'Migraine'),
        ('BLOATING', 'Bloating'),
        ('SPOTTING', 'Spotting'),
        ('CRAMPS', 'Cramps'),
        ('FATIGUE', 'Fatigue'),
        ('MOODSWINGS', 'Mood swings'),
        ('PIMPLES', 'Pimples'),
        ('PAINOV', 'Ovulation pain'),
        ('PAINBACK', 'Back pain'), 
        ('PAINAB', 'Abdominal pain'),
    )
    
    BC_METHOD = (
        ('NONE', 'None'),
        ('PILL', 'Pill'),
        ('MPILL', 'Minipill'),
        ('IUDH', 'Hormonal IUD'),
        ('IUDC', 'Copper IUD'),
        ('RING', 'Ring'),
        ('IMPLANT', 'Implant'),
        ('SHOT', 'Shot'),
        ('PATCH', 'Patch'),
        ('BARRIER', 'Barrier methods (condom, cervical cap, etc.)'),
        ('FAM', 'Fertility Awareness Method or Rythym Method'),
        ('WITHDRAWAL', 'Withdrawal'),
    )
    
    GOAL = (
        ('CONCEPTION', 'To get pregnant'),
        ('CONTRACEPTION', 'To avoid pregnancy'),
        ('CYCLEAWARENESS', 'Cycle awareness'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    date_of_last_menstrual_period = models.DateField(default=date.today)
    typical_flow_length = models.IntegerField()
    typical_cycle_length = models.IntegerField()
    typical_symptoms = MultiSelectField(choices=SYMPTOMS)
    current_birth_control_method = MultiSelectField(choices=BC_METHOD)
    # hormonal_therapy = models.Choices()
    goal = models.CharField(max_length=100, choices=GOAL) 
    
    def __str__(self):
        return self.first_name

class Event(models.Model):
    SYMPTOMS = (
        ('NONE', 'None'),
        ('HEADACHE', 'Headaches'),
        ('MIGRAINE', 'Migraine'),
        ('BLOATING', 'Bloating'),
        ('SPOTTING', 'Spotting'),
        ('FATIGUE', 'Fatigue'),
        ('PIMPLES', 'Pimples'),
        ('PAINOV', 'Ovulation pain'),
        ('PAINBACK', 'Back pain'), 
        ('PAINAB', 'Abdominal pain'),
    )

    CRAMPS = (
        ('NONE', 'None'),
        ('SLIGHT', 'Slight'),
        ('MODERATE', 'Moderate'),
        ('SEVERE', 'Severe'),
    )

    FLOW = (
        ('NONE', 'None'),
        ('LIGHT', 'Light'),
        ('MODERATE', 'Moderate'),
        ('HEAVY', 'Heavy'),
        ('VHEAVY', 'Very heavy'),
    )

    SPERM_OR_INSEMINATION = (
        ('UNPROTECTED', 'Unprotected'),
        ('PROTECTED', 'Protected'),
        ('INSEMINATION', 'Insemination'),
    )

    PREG_TEST_RESULT = (
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative'),
    )

    CERVICAL_FLUID = (
        ('STICKY', 'Sticky, dry'),
        ('CREAMY', 'Creamy'),
        ('STRETCHY', 'Stretchy, clear, slippery'),
    )

    LIBIDO = (
        ('NONE', 'None'),
        ('LOW', 'Low'),
        ('MODERATE', 'Moderate'),
        ('High', 'High'),
    )

    MOOD = (
        ('DEPRESSED', 'Depressed'),
        ('ANXIOUS', 'Anxious'),
        ('SAD', 'Sad'),
        ('NUMB', 'Numb'),
        ('IRRITABLE', 'Irritable'),
        ('ANGRY', 'Angry'),
        ('SENSITIVE', 'Sensitive'),
        ('SERENE', 'Serene'),
        ('HAPPY', 'Happy'),
        ('EXCITED', 'Excited'),
        ('ECSTATIC', 'Ecstatic'),
    )

    ENERGY = (
        ('EXHAUSTED', 'Exhausted'),
        ('LOW', 'Low'),
        ('MODERATE', 'Moderate'),
        ('HIGH', 'High'),
        ('ENERGIZED', 'Energized'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    period_started = models.DateField(default=date.today, null=True, blank=True)
    period_ended = models.DateField(default=date.today, null=True, blank=True)
    symptoms = MultiSelectField(choices=SYMPTOMS, null=True, blank=True)
    mood = MultiSelectField(choices=MOOD, null=True, blank=True)
    energy = MultiSelectField(choices=ENERGY, null=True, blank=True)
    cramps = models.CharField(max_length=100, choices=CRAMPS, null=True, blank=True)
    flow = models.CharField(max_length=100, choices=FLOW, null=True, blank=True)
    libido = models.CharField(max_length=100, choices=LIBIDO, null=True, blank=True)
    sperm = models.CharField(max_length=100, choices=SPERM_OR_INSEMINATION, null=True, blank=True)
    result = models.CharField(max_length=100, choices=PREG_TEST_RESULT, null=True, blank=True)
    fluid = MultiSelectField(choices=CERVICAL_FLUID, null=True, blank=True)
    bbt = models.FloatField(null=True, blank=True)
    lh = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 


# PeriodEvent
class PeriodEvent(models.Model):
    FLOW = (
        ('LIGHT', 'Light'),
        ('MODERATE', 'Moderate'),
        ('HEAVY', 'Heavy'),
        ('VHEAVY', 'Very heavy'),
    )
    
    CRAMPS = (
        ('NONE', 'None'),
        ('SLIGHT', 'Slight'),
        ('MODERATE', 'Moderate'),
        ('SEVERE', 'Severe'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Period')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    cramps = models.CharField(max_length=100, choices=CRAMPS, null=True, blank=True)
    flow = models.CharField(max_length=100, choices=FLOW, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 


# symptom event
class SymptomEvent(models.Model):
    SYMPTOMS = (
        ('NONE', 'None'),
        ('HEADACHE', 'Headaches'),
        ('MIGRAINE', 'Migraine'),
        ('BLOATING', 'Bloating'),
        ('SPOTTING', 'Spotting'),
        ('FATIGUE', 'Fatigue'),
        ('PIMPLES', 'Pimples'),
        ('PAINOV', 'Ovulation pain'),
        ('PAINBACK', 'Back pain'), 
        ('PAINAB', 'Abdominal pain'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Symptoms')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    symptoms = MultiSelectField(choices=SYMPTOMS, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 


# sperm event
class SpermEvent(models.Model):
    SPERM_OR_INSEMINATION = (
        ('UNPROTECTED', 'Unprotected'),
        ('PROTECTED', 'Protected'),
        ('INSEMINATION', 'Insemination'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Sperm encounter')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    type_of_encounter = models.CharField(max_length=100, choices=SPERM_OR_INSEMINATION, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 


# fertility event
class FertilityEvent(models.Model):
    PREG_TEST_RESULT = (
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative'),
    )

    CERVICAL_FLUID = (
        ('STICKY', 'Sticky, dry'),
        ('CREAMY', 'Creamy'),
        ('STRETCHY', 'Stretchy, clear, slippery'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='fertility')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    pregnancy_test_result = models.CharField(max_length=100, choices=PREG_TEST_RESULT, null=True, blank=True)
    cerivcal_fluid_consistency = MultiSelectField(choices=CERVICAL_FLUID, null=True, blank=True)
    basal_body_temperature = models.FloatField(null=True, blank=True)
    luteinizing_hormone_level = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 


# libido event
class LibidoEvent(models.Model):
    LIBIDO = (
        ('NONE', 'None'),
        ('LOW', 'Low'),
        ('MODERATE', 'Moderate'),
        ('High', 'High'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='libido')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    libido = models.CharField(max_length=100, choices=LIBIDO, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 

# mood event
class MoodEvent(models.Model):
    MOOD = (
        ('DEPRESSED', 'Depressed'),
        ('ANXIOUS', 'Anxious'),
        ('SAD', 'Sad'),
        ('NUMB', 'Numb'),
        ('IRRITABLE', 'Irritable'),
        ('ANGRY', 'Angry'),
        ('SENSITIVE', 'Sensitive'),
        ('SERENE', 'Serene'),
        ('HAPPY', 'Happy'),
        ('EXCITED', 'Excited'),
        ('ECSTATIC', 'Ecstatic'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='mood')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    mood = MultiSelectField(choices=MOOD, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 

# energy event
class EnergyEvent(models.Model):
    ENERGY = (
        ('EXHAUSTED', 'Exhausted'),
        ('LOW', 'Low'),
        ('MODERATE', 'Moderate'),
        ('HIGH', 'High'),
        ('ENERGIZED', 'Energized'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='energy level')
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    energy = MultiSelectField(choices=ENERGY, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 

# class Event(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=200, default='event')
#     # created = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateField(default=date.today)
#     end_date = models.DateField(default=date.today)
    
#     period_event = models.ForeignKey(PeriodEvent, on_delete=models.CASCADE, null=True, blank=True)
#     symptom_event = models.ForeignKey(SymptomEvent, on_delete=models.CASCADE, null=True, blank=True)
#     sperm_event = models.ForeignKey(SpermEvent, on_delete=models.CASCADE, null=True, blank=True)
#     fertility_event = models.ForeignKey(FertilityEvent, on_delete=models.CASCADE, null=True, blank=True)
#     libido_event = models.ForeignKey(LibidoEvent, on_delete=models.CASCADE, null=True, blank=True)
#     mood_event = models.ForeignKey(MoodEvent, on_delete=models.CASCADE, null=True, blank=True)
#     energy_event = models.ForeignKey(EnergyEvent, on_delete=models.CASCADE, null=True, blank=True)

#     @property
#     def get_html_url(self):
#         url = reverse('event-update', args=(self.id,))
#         return f'<a href="{url}"> {self.title} </a>'