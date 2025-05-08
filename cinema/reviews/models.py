from django.db import models
from users.models import CustomUser
from movies.models import Movie
from django.core.validators import MinValueValidator,MaxValueValidator

class Review(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="reviews")
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','movie')

    def __str__(self):
        return f"نظر{self.user.username} برای {self.movie.title}"    