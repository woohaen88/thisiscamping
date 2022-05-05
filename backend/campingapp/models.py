from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CampingInfo(TimeStampedModel):
    title = models.CharField(max_length=20, null=False)
    review = models.CharField(max_length=200, null=False)
    visited_at = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ground_on = models.CharField(max_length=10)
    with_animal = models.CharField(max_length=10)
    kind_of_view = models.CharField(max_length=10)
    kind_of_camper = models.CharField(max_length=10)
    can_fire = models.CharField(max_length=10)
    atmosphere_star = models.IntegerField()
    facility_star = models.IntegerField()
    total_star = models.FloatField()
    image = models.ImageField(upload_to="camping/images/%Y/%m/%d", blank=True)

    def __str__(self):
        return f"{self.title}"


class Photo(models.Model):
    image = models.ImageField(upload_to="camping/images/%Y/%m/%d", blank=True)
    camping_info = models.ForeignKey(CampingInfo, on_delete=models.CASCADE, null=True)
