from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from pr_test.teams.api.views import TeamViewSet
from pr_test.teams.models import Team


class TeamTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com", username="testuser", password="12345"
        )
        return super().setUp()

    def test_team_create(self):
        self.assertEqual(Team.objects.count(), 0)
        request = self.factory.post("/api/teams/")
        force_authenticate(request, user=self.user)
        response = TeamViewSet.as_view({"post": "create"})(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Team.objects.count(), 1)

    def test_team_list(self):
        team = Team.objects.create()
        team.users.add(self.user)
        request = self.factory.get("/api/teams/")
        force_authenticate(request, user=self.user)
        response = TeamViewSet.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)
        expected_data = [{"id": team.id}]
        self.assertEqual(response.data, expected_data)

    def test_team_list_another_user(self):
        team = Team.objects.create()
        team.users.add(self.user)
        another_user = get_user_model().objects.create_user(
            email="testuser2@test.com", username="testuser2", password="12345"
        )
        request = self.factory.get("/api/teams/")
        force_authenticate(request, user=another_user)
        response = TeamViewSet.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_team_join(self):
        team = Team.objects.create()
        request = self.factory.post(f"/api/teams/{team.id}/join/")
        force_authenticate(request, user=self.user)
        response = TeamViewSet.as_view({"post": "join"})(request, pk=team.id)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.user.teams.count(), 1)
