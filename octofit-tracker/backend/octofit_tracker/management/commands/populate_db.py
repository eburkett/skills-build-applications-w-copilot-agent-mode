from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for direct population if not already present
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')

        # Activities
        Activity.objects.create(user='ironman', team='Marvel', type='Run', duration=30)
        Activity.objects.create(user='batman', team='DC', type='Swim', duration=45)
        Activity.objects.create(user='wonderwoman', team='DC', type='Bike', duration=60)
        Activity.objects.create(user='spiderman', team='Marvel', type='Yoga', duration=20)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=50)
        Leaderboard.objects.create(team='DC', points=70)

        # Workouts
        Workout.objects.create(name='Super Strength', difficulty='Hard')
        Workout.objects.create(name='Speed Run', difficulty='Medium')
        Workout.objects.create(name='Stealth Swim', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
