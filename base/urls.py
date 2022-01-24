from django.contrib.auth import views
from django.urls import path
from . import views
from .views import EventList, EventDetail, EventCreate, PeriodEventCreate, SymptomEventCreate, SpermEventCreate, FertilityEventCreate, LibidoEventCreate, MoodEventCreate, EnergyEventCreate, EventUpdate, DeleteView, CustomLoginView, ProfileCreate, RegisterPage, CalendarView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile-form/', ProfileCreate.as_view(), name='profile-create'),
    path('', views.home, name='home'),
    path('calendar/', CalendarView.as_view(), name = 'calendar'),
    path('events', EventList.as_view(), name='events'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event'),
    path('event-create/', EventCreate.as_view(), name='event-create'),
    path('periodevent_form/', PeriodEventCreate.as_view(), name='period'),
    path('symptomevent_form/', SymptomEventCreate.as_view(), name='symptoms'),
    path('spermevent_form/', SpermEventCreate.as_view(), name='sperm'),
    path('fertilityevent_form/', FertilityEventCreate.as_view(), name='fertility'),
    path('libidoevent_form/', LibidoEventCreate.as_view(), name='libido'),
    path('moodevent_form/', MoodEventCreate.as_view(), name='mood'),
    path('energyevent_form/', EnergyEventCreate.as_view(), name='energy'),
    path('event-update/<int:pk>/', EventUpdate.as_view(), name='event-update'),
    path('event-delete/<int:pk>/', DeleteView.as_view(), name='event-delete'),
    path('profile/', views.profile_view, name='profile'),
    path('snapshot/', views.snapshot, name='snapshot'),
    path('about/', views.about, name='about'),
] 