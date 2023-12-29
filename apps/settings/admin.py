from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.settings.models import Pricing, Procurement, Jobs, History, Banner, BankDetails
# Register your models here.
class PricingAdmin(TranslatableAdmin):
    list_display = ('payment',)
    fieldsets = (
        (None, {
            'fields': ('payment', 'taxes', 'ai_80', 'disel', 'mazmut'),
        }),
        
    )
admin.site.register(Pricing, PricingAdmin)

class HistoryAdmin(TranslatableAdmin):
    list_display = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date'),
        }),
        
    )
admin.site.register(History, HistoryAdmin)

class JobsAdmin(TranslatableAdmin):
    list_display = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'requirements'),
        }),
        
    )
admin.site.register(Jobs, JobsAdmin)

class ProcurementAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'requirements'),
        }),
        
    )
admin.site.register(Procurement, ProcurementAdmin)
admin.site.register(BankDetails)
admin.site.register(Banner)