from django.contrib import admin
from movielist_app.models import WatchList, StreamPlatform

# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamPlatform)