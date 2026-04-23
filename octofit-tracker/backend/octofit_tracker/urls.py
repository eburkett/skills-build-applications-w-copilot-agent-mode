"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('users/'),
        'teams': request.build_absolute_uri('teams/'),
        'activities': request.build_absolute_uri('activities/'),
        'leaderboard': request.build_absolute_uri('leaderboard/'),
        'workouts': request.build_absolute_uri('workouts/'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api_root'),
    path('', include(router.urls)),
]

@method_decorator(csrf_exempt, name='dispatch')
class TeamListView(View):
    def get(self, request):
        teams = list(Team.objects.values('name'))
        return JsonResponse(teams, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class ActivityListView(View):
    def get(self, request):
        activities = list(Activity.objects.values())
        return JsonResponse(activities, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class LeaderboardListView(View):
    def get(self, request):
        leaderboard = list(Leaderboard.objects.values())
        return JsonResponse(leaderboard, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class WorkoutListView(View):
    def get(self, request):
        workouts = list(Workout.objects.values())
        return JsonResponse(workouts, safe=False)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserListView.as_view()),
    path('api/teams/', TeamListView.as_view()),
    path('api/activities/', ActivityListView.as_view()),
    path('api/leaderboard/', LeaderboardListView.as_view()),
    path('api/workouts/', WorkoutListView.as_view()),
]
