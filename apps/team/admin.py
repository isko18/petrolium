from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.team.models import Team
# Register your models here.
class TeamAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {
            'fields': ('full_name', 'job_title', 'image'),
        }),
        
    )
admin.site.register(Team, TeamAdmin)
