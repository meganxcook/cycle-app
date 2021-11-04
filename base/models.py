from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import date


class Profile(models.Model):
    SYMPTOMS = (
        ('NONE', 'None'),
        ('HEADACHE', 'Headache'),
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
    lmp = models.DateField(default=date.today)
    typical_flow_length = models.IntegerField()
    typical_cycle_length = models.IntegerField()
    typical_symptoms = MultiSelectField(choices=SYMPTOMS)
    current_bc_method = MultiSelectField(choices=BC_METHOD)
    goal = models.CharField(max_length=100, choices=GOAL) 
    
    def __str__(self):
        return self.first_name

# dennis ivy to do app tutorial
# class Event(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# hui wen calendar tutorial
class Event(models.Model):
    SYMPTOMS = (
        ('NONE', 'None'),
        ('HEADACHE', 'Headaches'),
        ('MIGRAINE', 'Migraines'),
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
        ('LIGHT', 'Light'),
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
        ('YES', 'Yes'),
    )

    PREG_TEST_RESULT = (
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative'),
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
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    period_started = models.DateField(default=date.today, null=True, blank=True)
    period_ended = models.DateField(default=date.today, null=True, blank=True)
    symptoms = MultiSelectField(choices=SYMPTOMS, null=True, blank=True)
    mood = MultiSelectField(choices=MOOD, null=True, blank=True)
    cramps = models.CharField(max_length=100, choices=CRAMPS, null=True, blank=True)
    flow = models.CharField(max_length=100, choices=FLOW, null=True, blank=True)
    libido = models.CharField(max_length=100, choices=LIBIDO, null=True, blank=True)
    sperm = models.CharField(max_length=100, choices=SPERM_OR_INSEMINATION, null=True, blank=True)
    result = models.CharField(max_length=100, choices=PREG_TEST_RESULT, null=True, blank=True)
    bbt = models.FloatField(null=True, blank=True)
    lh = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event-update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title 