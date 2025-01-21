from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.CharField(max_length=1)
    

    
    

