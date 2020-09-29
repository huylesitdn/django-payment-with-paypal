from django.db import models

# Create your models here.
class Plan(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  limit = models.BooleanField(default=True)
  role = models.CharField(max_length = 150, null=True, blank=True, choices=[
    ('Monthly', 'monthly'),
    ('Yearly', 'yearly')
  ])

  def __str__(self):
    return self.name
  