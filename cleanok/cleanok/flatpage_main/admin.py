from django.contrib import admin
from flatpage_main.models import MyFlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.forms import FlatpageForm
from django.utils.translation import gettext_lazy as _

class FlatPageAdmin(FlatPageAdmin):
    
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url' , 'description', 'desc_items', 'sites')}),
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title')

admin.site.unregister(FlatPage)
admin.site.register(MyFlatPage, FlatPageAdmin)