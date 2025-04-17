from django.db import models
import uuid

# Create your models here.

class Tips(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    total_bill = models.FloatField(default=0)
    sex = models.CharField(max_length=24)
    smoker = models.CharField(max_length=24)
    day = models.CharField(max_length=24)
    time = models.CharField(max_length=24)
    size = models.FloatField(default=0)
    tip = models.CharField(max_length=20)

    def __str__(self):
        return(f"{str(self.id)}:{self.total_bill}")

