from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Services
from .serializers import ServicesSerializer

class NearestServiceAPI(APIView):
    def post(self, request):
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        service_type = request.data.get('service_type')
        
        # User location as a GEOS Point
        user_location = Point(float(lng), float(lat), srid=4326)

        
        nearest_services = Services.objects.filter(
            service_type=service_type,
            service_location__dwithin=(user_location, 5000) 
        ).annotate(
            distance=Distance('service_location', user_location)
        ).order_by('distance')[:20]  # Limit to top 20 nearest for performance

        serializer = ServicesSerializer(nearest_services, many=True)
        return Response(serializer.data)

def PageApp(request):
    return render(request, 'index.html')