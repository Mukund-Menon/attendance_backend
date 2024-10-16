from django.db import models
import uuid

class Attendee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    intime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attendee.name} - {self.intime}"