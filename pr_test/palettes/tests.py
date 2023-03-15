from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from pr_test.palettes.api.views import PaletteViewSet


class TestPalette(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com", username="testuser", password="12345"
        )
        return super().setUp()

    def test_palette_create(self):
        request = self.factory.post(
            "/api/palettes/", {"name": "test", "colors": ["#000000"]}
        )
        force_authenticate(request, user=self.user)
        response = PaletteViewSet.as_view({"post": "create"})(request)
        self.assertEqual(response.status_code, 201)

    def test_palette_create_invalid_colors_too_short(self):
        request = self.factory.post(
            "/api/palettes/", {"name": "test", "colors": ["#00000"]}
        )
        force_authenticate(request, user=self.user)
        response = PaletteViewSet.as_view({"post": "create"})(request)
        self.assertEqual(response.status_code, 400)

    def test_palette_create_invalid_colors_string(self):
        request = self.factory.post(
            "/api/palettes/", {"name": "test", "colors": ["itsastring"]}
        )
        force_authenticate(request, user=self.user)
        response = PaletteViewSet.as_view({"post": "create"})(request)
        self.assertEqual(response.status_code, 400)

    def test_empty_palette_list(self):
        request = self.factory.get("/api/palettes/")
        force_authenticate(request, user=self.user)
        response = PaletteViewSet.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_palette_list(self):
        palette = self.user.palettes.create(name="test", colors=["#000000"])
        request = self.factory.get("/api/palettes/")
        force_authenticate(request, user=self.user)
        response = PaletteViewSet.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)
        expected_data = [{"id": palette.id, "name": "test", "colors": ["#000000"]}]
        self.assertEqual(response.data, expected_data)

    def test_palette_list_another_user(self):
        palette = self.user.palettes.create(name="test", colors=["#000000"])
        another_user = get_user_model().objects.create_user(
            email="testuser2@test.com", username="testuser2", password="12345"
        )
        another_user.palettes.create(name="test2", colors=["#000001"])
        request = self.factory.get("/api/palettes/")
        force_authenticate(request, user=self.user)
        response = PaletteViewSet.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)
        expected_data = [{"id": palette.id, "name": "test", "colors": ["#000000"]}]
        self.assertEqual(response.data, expected_data)
