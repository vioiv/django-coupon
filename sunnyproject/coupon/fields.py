import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile

class CouponImageField(ImageFieldFile):
    def save(self, name, content, save=True):
        super().save(name, content, save)

    def delete(self, save=True):
        super().delete(save)

class CouponImageField(ImageField):
    def __init__(self, verbose_name=None, **kwargs):
        super().__init__(verbose_name, **kwargs)