# CYCLE APP
## By Megan Cook
## Created 10/8/2021
_______________________________________________

- [x] Python
- [x] HTML
- [x] CSS
- [x] JavaScript
- [x] Django

_______________________________________________
## 1. Project Overview

**Name: Cycle. App**

**Description:** An inclusive, evidence-based menstrual cycle tracking app for queer, trans, non-binary, gender-fluid or otherwise gender non-conforming individuals who want to get pregnant, prevent pregnancy, or gain better awareness of their cycle. 

**What problem does this app solve?**

The menstrual cycle tracking apps that are currently on the market are targeted mostly to cis women and feel exlusive of non cis gendered people. Not everyone who menstruates and gives birth identifies as a woman, and certain individuals may be experiencing specific hormonal situations. Queer, trans, and NB folks have unique needs and challenges when it comes to conception and contraception that no app on the market currently addresses. 

Cycle. App uses neutral color schemes and neutral and inclusive language. Almost every feature is customizable so the user can track only items they want to track depending on their specific goal.

**Major features:**
1. Color-coded calendar representing each day of the cycle. 
2. Ability to log and track important events, signs, and symptoms (when cycle begins/ends, encounters with sperm, basal body temp, mood swings, headaches, cramps, etc.).
3. User profile with personalized features (cycle length, flow length, goal).
4. In app alerts and reminders for phase of cycle (predicted mentstrual, follicular, ovulation, luteal phase dates), to take contraception, to take BBT.
5. Ability to predict and adjust cycle and flow length based on user input over time.
6. Data points plotted on graphs to provide visual feedback over time.
7. Ability to toggle most features on and off to see only what the user wants to see.

**Libraries:**
~~* [Django Scheduler](https://pypi.org/project/django-scheduler/)
* [Python Calendar](https://docs.python.org/3/library/calendar.html)~~
* [Python Lunar](https://pypi.org/project/pylunar/)

**Tutorials:**
* <https://uggedal.com/journal/creating-a-flexible-monthly-calendar-in-django/>
* <https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html>

**Framesworks:**
* Django

**APIs:**
* [Moon phases](https://www.aerisweather.com/support/docs/api/reference/endpoints/sunmoon-moonphases/)
* [Weather data](https://www.visualcrossing.com/weather/weather-data-services#/apiquery)


## 2. Functionality (views)

**Register**
* username
* password
* email
* first name

**Login**
* username
* password

**1. Register new user:**
* Prompt user to enter info:
    * When did your last menstrual cycle begin?
        * Select date (start with today's date)
        * I don't get a period right now
        * I don't know 
    * Cycle info:
        * How many days does menstruation usually last?
            * Select number between 3 and 10
            * 15+ days (special settings)
            * Don't know (set default date to 6 days)
        * How many days does your full cycle typically last?
            * Enter number between 0-59 
            * 60+ days (special settings) 
            * Don't know (set default to 28 days for cycle length)
            * It varies (set default to 28 days for cycle length; special settings)
        * Which symptoms do you typically experience, if any?
            * SYMPTOMS (from Models)
    * Goal (select):
        * I want to get pregnant
        * I want to avoid pregnancy
        * I want to gain awareness around my cycle
    * Are you currently using birth control or contraception?
        * No
        * Yes:
            * BC_METHOD (from Models)
    * Are you currently on testosterone or other hormonal treatments?
        * No
        * Yes (more to do here)

**2. Home:** 
* Logo
* Menu (left, hamburger, collapsible):
    * Home
    * About
    * Log out
* Sections:
    1. Greeting (user's first name)
    2. Today's date and current moon phase (emoji + words)  
    3. Current:
        * User's current phase
        * Day number
    4. Upcoming:
        * Ovulation
        * Menstruation
    5. Reminders (check boxes to be completed by user; depending on goal and features toggled on):
        * Take contraception
        * Log BBT today (alert)
        * Test LH in 5 days
* Recommendations (synced with user's current phase):
    1. Menstruation:
        * This phase is similar to winter. Hormone levels are low. It's a good time to hibernate.
            * Take some time and space to turn inward; rest, reflect, and recharge.
            * Focus on self-care this week.
            * Research.
    2. Follicular phase:
        * Think of this phase as spring. Estrogen is rising. It's a good time to think about the big picture.
            * Plan social engagements for the upcoming week.
            * Start making a few moves. 
            * Create and plan. 
    3. Ovulatory phase:
        * Welcome to the summer of your cycle. The event of ovulation typically occurs around day 14 of your cycle. The ovulatory phase may begin about 5 days before ovulation and end about 2 days after ovulation. This is when hormone levels peak. It's a good time to be social.
            * Engage in activites that bring you pleasure and joy.
            * Seek connection; communicate and collaborate with others.
            * Now is the time to take action and implement your plans.
            * Play and execute.
    4. Luteal phase:
        * This phase is the fall or autumn of your cycle. Estrogen is dropping and progesterone is rising. It's a good time to focus on completion. 
            * Slow down and tend to your nest.
            * Get organized and wrap things up.
            * Focus.

**3. Calendar**
* Moon phases auto populated
* Days are clickable
* See all events logged on each day, color coded
* Click event to update or view details

**4. Log Event**
* Show current date, moon phase
* Show current phase and cycle day number
    * Menstrual phase: day 0-5
    * Follicular phase: day 5-9
    * Ovulatory phase: day 10-16
        * Ovulation: day 14
    * Luteal phase: day 17-28
* User can log events, signs, and symptoms
    * Events: 
        * Encounter with sperm:
            * With or without protection (do not ask about protection if goal is conception)
        * Pregnancy test result
        * Basal Body Temperature (BBT)
        * Mid-cycle ovulation pain
        * Spotting/breakthrough bleeding
    * Signs/Symptoms*:
        * None
        * Headache
        * Migraine
        * Mood swings
        * Bloating
        * Pimples
        * Fatigue
        * Cramps
        * Spotting
        * Painful ovulation
        * Back pain
        * Abdominal pain
        * (Look up and include thyroid, PCOS, endmetriosis, cortisol imbalance symptoms)
    * Notes (user can enter notes to themself)

**5. Snapshot**
* Scales (collect points of data then display on chart):
    * BBT chart (important feature!)
    * LH
    * Flow (light, moderate, heavy)
    * Cramps (none, light, moderate, heavy)
    * Libido (low, moderate, high)
    * Mood (depressed, sad, numb, irritable, angry, sensitive, happy, excited, manic)
    * Energy level (exhausted, low, moderate, high, energized)

**6. Profile:** 
* User's name
    * Update profile button
* User's goal:
    * Update goal button
* Cycle overview:
    * Typical cycle length
    * Typical flow length
* Recurrent symptoms (list of 3-5)
* Current method of contraception
    * Update contraception button
* Reset password button
* Log out button

**7. About:** 
* About the app
* Resource list of links 
* Contact (help, feedback)

<!-- **8. Day view (view a specific date):** 
* Show all events for a specific day  -->


## 3. Models

1. Model 1: **Profile**
    * BC list:
        * Pill
        * Minipill
        * Hormonal IUD
        * Copper IUD
        * Ring
        * Implant
        * Shot
        * Patch
        * Barrier methods (condoms, cervical cap, etc.)
        * Fertility Awareness Method or Rythym Method
        * Withdrawal
        * Not sure
    * Fields:
        * Date of last menstrual period
        * Typical cycle length (number; default = 28 days)
        * Typical flow length (number; default = 5 days)
        * Goal (select: contraception, conception, cycle awareness)
        * Current contraception  

2. Model 2: **Cycle**
    * Fields:
        * Cycle start date
        * Menstruation end date
        * Events
        * Signs/symptoms
        * Scales
        * Notes
    * (ForeignKey that references Model 1)

3. Model 3: **Event**
    * Menstruation start date (DateField)
    * Menstruation end date
    * Encounter with sperm
    * Pregnancy test result
    * BBT
    * LH
    * Symptoms list
    * Flow
    * Cramps
    * Libido
    * Mood

4. Model 4: **Default Dates**
    * Menstrual phase: day 0-5
    * Follicular phase: day 5-9
    * Ovulatory phase: day 10-16
        * Ovulation: day 14
    * Luteal phase: day 17-28

## 4. Views
**How to do predicted dates?**
* Menstrual Phase
* Follicular Phase
* Ovulation
* Luteal Phase
* 3 day warning before menstrual phase


## 5. Schedule

1. Milestone #1: 
    - [x] Django server running
    - [x] Brand assets
    - [x] Bottom navigation bar 
    - [x] Calendar layout

2. Milestone #2: 
    - [x] Register new user page
    - [ ] Add events/symptoms using forms and widgets
    - [x] Calendar working
    - [x] Top toggle navigation menu
    - [x] Links working
    - [ ] Stats page

3. Milestone #3: 
    - [ ] Profile page
    - [ ] Contact page
    - [ ] About page
    - [ ] Connect models and views
    - [ ] Create multiple users and test
    - [ ] Day view
    - [ ] CSS
    - [ ] JS

4. Milestone #4: 
    - [ ] Polish details
    - [ ] Presentation

**Post-presentation:**    
* Test app on fertility course participants; eventually list in marketplace. 
* Gather feedback from users; make this a community created project; bring on skilled collaborators.
* Features to add: 
    * Guidance on how to manage symptoms and balance hormones (from licensed midwives/fertility experts)
    * Tell user how their cycle lines up with moon phases and explain what that means
    * Improve predictive features (moods, symptoms, charts, scales)
    * iCal/Google cal export/syncing
* Develop inclusive pregnancy app for queer/trans/NB people to track fetal development.

__________________________________________
## NOTES

**Cycle Tracker App:**
* Create user accounts
* Count
* Click on date
* Calendar or circle?
* Python/django libraries to display calendars
* Implement django rest

**Inspiration Apps:**
* [Modern Fertility](https://modernfertility.com/)
* Kindara
* Clue
* [Egg Timer](https://github.com/jessamynsmith/eggtimer-server)

**Community Feedback:**
* What features would you like to see in a cycle tracking app?
* What language or specific words do you want to see in the app?
* What type of language, specific words, colors, images do you NOT want to see in the app?
* What types of notifications/alerts do you prefer? What do you not like? 

**Sources:**
* [Five things to think about when designing a period tracking app](https://medium.com/hci-design-at-uw/five-things-to-think-about-when-designing-a-period-tracking-app-9a79ac7cf446)
* [Hui Wen (Calendar)](https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html)
* [Dennis Ivy (Class Based Views, Registration, Login, CRUD)](https://www.youtube.com/watch?v=llbtoQTt4qw&t=5249s&ab_channel=DennisIvy)
* [Mostafa Elgayar (MultiSelectField)](https://www.youtube.com/watch?v=5jWJBpS0tkg&ab_channel=MostafaElgayar)
* [Jason Sturges (Moon phases & emojis)](https://github.com/jasonsturges/lunarphase-js) 
* [Kevin Powell (Styling)](https://www.youtube.com/watch?v=_xkSvufmjEs&list=PL2_TKXd2NxCntHuq63-Uad6pfa3aZd3B4&index=2&t=485s&ab_channel=freeCodeCamp.org)
* dcode (bottom navigation bar)
* Deltaty (hamburger menu)
* (buttons)