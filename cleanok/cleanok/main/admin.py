from django.contrib import admin
from main.models import *

# Register your models here.

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'approved')
    list_filter = ('approved', )

admin.site.register(ShortInfoAboutCompany)
admin.site.register(InfoItem)
admin.site.register(Service)
admin.site.register(ServiceWorksNames)
admin.site.register(SpecialService)
admin.site.register(SpecialServiceWorksNames)
admin.site.register(WhyWe)
admin.site.register(OrderRequest)