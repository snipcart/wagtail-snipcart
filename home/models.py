from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

class Product(Page):
    productAt = models.URLField()
    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('sku'),
        FieldPanel('productAt'),
        FieldPanel('name'),
        FieldPanel('image'),
        FieldPanel('price'),
        FieldPanel('description')
    ]

@register_setting
class SnipcartSettings(BaseSetting):
    ApiKey = models.CharField(
        max_length=255,
        help_text='Your Snipcart Api Key'
    )
