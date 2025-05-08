from django.db import models
from movies.models import Movie

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.name
    
class Theater(models.Model):
    Cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE,related_name="theaters")    
    name = models.CharField(max_length=50)
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.Cinema.name} - {self.name}"
    

class Showtime(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="showtimes")
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name="showtimes")
    start_time = models.DateTimeField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} در {self.theater} - {self.start_time}"
    
    
