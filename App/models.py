from django.contrib.gis.db import models

# Create your models here.
class Services(models.Model):
    service = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50)
    service_location = models.PointField(srid=4326)
    
class UserQuery(models.Model):
    user_location = models.PointField(srid=4326)
    nearest_service = models.ForeignKey(Services , on_delete=models.CASCADE)
    distance_m = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
