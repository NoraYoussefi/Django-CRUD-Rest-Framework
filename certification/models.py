from django.db import models

class certification_model(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    bg_photo = models.CharField(max_length=200,blank=False, default='')
    user_name = models.CharField(max_length=20, blank=False, default='')
    date = models.CharField(max_length=20, blank=False, default='')
   
   
    # certificat   user  competition
# class competition_model(models.Model):
#     title = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200,blank=False, default='')
#     bg_photo = models.CharField(max_length=200,blank=False, default='')
    