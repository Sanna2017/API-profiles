from django.contrib import admin #already there

from . models import UserProfile
admin.site.register(UserProfile)
