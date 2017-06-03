from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', blank=True)
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.FileField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Project(models.Model):
    MY_CHOICES2 = ((1, 'Hardware'),
               (2, 'Software'),
               (3, 'Both'))

    author = models.ForeignKey('auth.User', blank=True)
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    HorS = MultiSelectField(choices=MY_CHOICES2,
                                 max_choices=1,
                                 max_length=3)
    image = models.FileField()
    repoLink = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
