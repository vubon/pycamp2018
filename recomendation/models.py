from django.db import models
from userprofile.models import PersonalProfile
from events.models import EventBasic


# Create your models here.



class PersonalRecomendation(models.Model):
    profile_id = models.ForeignKey(PersonalProfile,on_delete=models.CASCADE)
    trainer_id = models.ForeignKey(PersonalProfile,on_delete=models.CASCADE)
    event_id = models.ForeignKey(EventBasic,on_delete=models.CASCADE)
    remarks = models.TextField()
    status= models.BooleanField(default=True)
