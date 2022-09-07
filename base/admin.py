from atexit import register
from django.contrib import admin
from base.models import player,evening

# Register your models here.
admin.site.register(player)
admin.site.register(evening)
