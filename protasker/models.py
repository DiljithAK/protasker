from django.db import models

class Tasks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return "name: " + self.name + ", description: " + self.description + ", status: " + str(self.status)
