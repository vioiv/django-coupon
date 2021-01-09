from django.shortcuts import render

from django.views.generic import ListView
from coupon.models import Coupon

class CouponLV(ListView):
    model = Coupon