from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        user1 = User.objects.create(email="thundergod@mhigh.edu", name="Thor", age=1500)
        user2 = User.objects.create(email="metalgeek@mhigh.edu", name="Tony Stark", age=48)
        user3 = User.objects.create(email="zerocool@mhigh.edu", name="Steve Rogers", age=105)
        user4 = User.objects.create(email="crashoverride@mhigh.edu", name="Natasha Romanoff", age=35)
        user5 = User.objects.create(email="sleeptoken@mhigh.edu", name="Bruce Banner", age=50)

        # Create teams
        team1 = Team.objects.create(name="Avengers")
        team1.members.add(user1, user2, user3, user4, user5)

        # Create activities
        Activity.objects.create(user=user1, activity_type="Cycling", duration=60, date=date(2025, 4, 9))
        Activity.objects.create(user=user2, activity_type="Crossfit", duration=120, date=date(2025, 4, 9))
        Activity.objects.create(user=user3, activity_type="Running", duration=90, date=date(2025, 4, 9))
        Activity.objects.create(user=user4, activity_type="Strength", duration=30, date=date(2025, 4, 9))
        Activity.objects.create(user=user5, activity_type="Swimming", duration=75, date=date(2025, 4, 9))

        # Create leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=90)
        Leaderboard.objects.create(user=user3, score=95)
        Leaderboard.objects.create(user=user4, score=85)
        Leaderboard.objects.create(user=user5, score=80)

        # Create workouts
        Workout.objects.create(user=user1, workout_name="Cycling Training", calories_burned=500)
        Workout.objects.create(user=user2, workout_name="Crossfit Session", calories_burned=700)
        Workout.objects.create(user=user3, workout_name="Marathon Training", calories_burned=600)
        Workout.objects.create(user=user4, workout_name="Strength Training", calories_burned=300)
        Workout.objects.create(user=user5, workout_name="Swimming Laps", calories_burned=400)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
