from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Player(models.Model):
    positions = {
        (0,'Bramkarz'),
        (1,'Obrońca'),
        (2,'Pomocnik'),
        (3,'Napastnik')
    }
    name = models.CharField(max_length=30,null=False,blank=False)
    surname = models.CharField(max_length=40,null=False,blank=False)
    weight = models.DecimalField(max_digits=4, decimal_places=1,null=False,blank=False)
    height = models.PositiveSmallIntegerField(null=False,blank=False)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False,null=False,blank=False)
    position = models.PositiveSmallIntegerField(default=0, choices = positions)
    photo = models.ImageField(upload_to='players_photos',null=True,blank=True)

    def __str__(self):
        return self.key_data()
    
    def key_data(self):
        def swich(position):
            if position ==0:
                return 'BR'
            elif position ==1:
                return 'OB'
            elif position ==2:
                return 'PM'
            elif position ==3:
                return 'N'

        position = swich(self.position)
        return "{}. {} ({})".format(self.name[0], self.surname, position)
        

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    poster = models.ImageField(upload_to='poster',null=True,blank=True)
    date_of_publication = models.DateField(auto_now_add=True, blank=False, null=False)
    creator = models.ForeignKey(User, default=1,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.key_data()
    
    def key_data(self):
        add = ''
        if len(self.title)>20:
            add = '(..)'
        return "{}{} - {}".format(self.title[ :20],add,self.date_of_publication)