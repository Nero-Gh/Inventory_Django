from django.contrib import admin
from .models import Product,Order

#Style admin dashboard here
admin.site.site_header="NeroInventory Dashboard"

class ProductAdmin(admin.ModelAdmin):  #Changing Product style into table form
    list_display=('id','name','category','quantity')
    list_filter=('category',)

class OrderAdmin(admin.ModelAdmin):  #Changing Product style into table form
    list_display=('id','product','staff','order_quantity','date')
    list_filter=('product',)




# Register your models here.
admin.site.register(Product,ProductAdmin)

admin.site.register(Order,OrderAdmin)
