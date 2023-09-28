from django.contrib import admin
from .models import Player,Article

# Register your models here.
admin.site.register(Player)

class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'date_of_publication', 'content', 'creator']
    

admin.site.register(Article)