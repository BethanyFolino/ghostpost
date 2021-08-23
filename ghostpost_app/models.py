from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    boast_or_roast = models.BooleanField() # boast or roast setup
    text = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    @property
    def vote_score(self):
        return self.upvotes - self.downvotes
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name