from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemInLine(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInLine, )


admin.site.register(Order, OrderAdmin)