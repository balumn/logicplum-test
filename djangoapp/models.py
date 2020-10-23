from django.db import models
from datetime import datetime

# Create your models here.
class ApiCall(models.Model):
    name        = models.CharField(max_length=100)
    method      = models.CharField(max_length=100)
    status_code = models.IntegerField()
    result      = models.CharField(max_length=100)
    created_at  = models.DateTimeField(default=datetime.now,verbose_name="Timestamp")
    
    def __str__(self):
        return self.method +"\t"+ self.name +"\t"+ str(self.status_code)