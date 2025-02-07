from django.db import models


# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.title
