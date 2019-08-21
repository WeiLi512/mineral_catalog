from django.db import models

# Create your models here.
class Mineral(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image_filename = models.CharField(max_length=200, blank=True)
    image_caption = models.TextField()
    category = models.CharField(max_length=200, blank=True)
    formula = models.TextField()
    strunz_classification = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=200, blank=True)
    crystal_system = models.CharField(max_length=200, blank=True)
    unit_cell = models.CharField(max_length=200, blank=True)
    crystal_symmetry = models.CharField(max_length=200, blank=True)
    cleavage = models.CharField(max_length=200, blank=True)
    mohs_scale_hardness = models.CharField(max_length=200, blank=True)
    luster = models.CharField(max_length=200, blank=True)
    streak = models.CharField(max_length=200, blank=True)
    diaphaneity = models.CharField(max_length=200, blank=True)
    optical_properties = models.CharField(max_length=200, blank=True)
    refractive_index = models.CharField(max_length=200, blank=True)
    crystal_habit = models.CharField(max_length=200, blank=True)
    specific_gravity = models.CharField(max_length=200, blank=True)
    group = models.CharField(max_length=200, blank=True)