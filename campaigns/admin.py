from django.contrib import admin
from .models import Campaign, Subscriber


class CampaignModelAdmin(admin.ModelAdmin):
    list_display=('title', 'created_at', 'updated_at')
    search_fields=('title','description')
    list_per_page=25


class SubscriberModelAdmin(admin.ModelAdmin):
    list_display=('email', 'campaign', 'created_at')
    search_fields=('email','campaign')
    list_per_page=25



admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(Subscriber, SubscriberModelAdmin)