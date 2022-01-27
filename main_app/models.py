from django.db import models
from django.urls import reverse

# Create your models here.

class Outfit(models.Model):
    style = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.style

    def get_absolute_url(self):
        return reverse('outfits_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    outfits = models.ManyToManyField(Outfit)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

ACTIVITIES = (
    ('P', 'Park'),
    ('R', 'Run'),
    ('W', 'Walk'),
)

class Exercise(models.Model):
    date = models.DateField('Exercise date')
    activity = models.CharField(
        max_length=1,
        choices=ACTIVITIES,
        default=ACTIVITIES[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return f"{self.get_activity_display()} on {self.date}"