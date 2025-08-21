from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, report_view, weather_view, echo_view

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
    path("report/", report_view, name="report"),
    path("weather/", weather_view, name="weather"),
    path("echo/", echo_view, name="echo"),
]
