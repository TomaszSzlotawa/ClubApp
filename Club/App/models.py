from django.db import models

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
        
