from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import TruncDate
from django.db.models import Count
from .models import Task
from .serializers import TaskSerializer
import requests

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.order_by("-created_at")
    serializer_class = TaskSerializer
    authentication_classes = []          
    permission_classes = [AllowAny]      

@api_view(["GET"])
def report_view(request):
    by_status = Task.objects.values("status").annotate(count=Count("id")).order_by("status")
    by_day = Task.objects.annotate(day=TruncDate("created_at")).values("day").annotate(count=Count("id")).order_by("day")
    return Response({"by_status": list(by_status), "by_day": list(by_day)})

@api_view(["GET"])
def weather_view(request):
    # Simple third-party API integration: Open-Meteo (no key required)
    # Example: /api/weather/?city=Pune
    city = request.GET.get("city", "Pune")
    try:
        geo = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city, "count": 1}).json()
        if not geo.get("results"):
            return Response({"error": "City not found"}, status=404)
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        weather = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": lat, "longitude": lon, "hourly": "temperature_2m"}).json()
        return Response({"city": city, "coords": {"lat": lat, "lon": lon}, "weather": weather})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["POST"])
def echo_view(request):
    # Example of sending data to a third-party echo API (postman-echo) and returning its response
    payload = request.data or {"message": "hello"}
    try:
        r = requests.post("https://postman-echo.com/post", json=payload, timeout=10)
        return Response({"sent": payload, "echo_response": r.json()})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
