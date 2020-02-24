from django.contrib import admin

# Register your models here.
from .models import Plot, Favorite, User

admin.site.register(Plot)
admin.site.register(User)
admin.site.register(Favorite)
