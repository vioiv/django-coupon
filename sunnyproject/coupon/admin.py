from django.contrib import admin
from coupon.models import Coupon

@admin.register(Coupon)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')