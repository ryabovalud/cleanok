from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


class MyFlatPage(FlatPage):
    
    description = models.TextField(_('Description'), blank=True)
    desc_items = models.TextField(_('Description items'), blank=True)