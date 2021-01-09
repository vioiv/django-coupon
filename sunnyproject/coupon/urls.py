from django.urls import path
from coupon import views

app_name = 'coupon'
urlpatterns = [
    # Example /coupon/
    path('', views.CouponLV.as_view())
]