from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Sport)
admin.site.register(players)
admin.site.register(tornament)