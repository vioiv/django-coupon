from django.db import models

from coupon.fields import CouponImageField

class Coupon(models.Model):
    title = models.CharField('TITLE', max_length=30)
    image = CouponImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)