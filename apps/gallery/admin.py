from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.gallery.models import Video, Photo
# Register your models here.
class VideoAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {
            'fields': ('title','video', 'screen_image', 'duration'),
        }),
        
    )
    
admin.site.register(Video, VideoAdmin)
admin.site.register(Photo)