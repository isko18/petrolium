# apps/news/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.management import call_command

from .models import News

@receiver(post_save, sender=News)
def restart_server_on_news_save(sender, instance, **kwargs):
    # This will be called whenever a News instance is saved
    call_command('runserver', '--noreload')  # Replace with your actual command
