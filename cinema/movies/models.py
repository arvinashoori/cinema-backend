from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text = 'مدت زمان به دقیقه')
    poster = models.ImageField(upload_to="posters/")
    genres = models.ManyToManyField(Genre,related_name='movies')
    director = models.CharField(max_length=100)
    avearge_rating = models.FloatField(default=0.0,validators=[MinValueValidator(0),MaxValueValidator(10)]) 

    def __str__(self):
        return self.title   