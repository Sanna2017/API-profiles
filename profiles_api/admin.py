from django.contrib import admin #already there

from . models import UserProfile, UserProfileManager,ProfileFeedItem
admin.site.register(UserProfile)
#admin.site.register(UserProfileManager) #cannot do this 
admin.site.register(ProfileFeedItem)
