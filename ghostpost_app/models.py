from django.db import models

# Create your models here.
class Post(models.Model):
    boast_or_roast = models.BooleanField() # boast or roast setup
    text = models.CharField(max_length=280)
    # votes =
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    submission_time = models.DateTimeField()