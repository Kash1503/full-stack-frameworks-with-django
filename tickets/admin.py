from django.contrib import admin
from .models import Ticket, Comments

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Comments)