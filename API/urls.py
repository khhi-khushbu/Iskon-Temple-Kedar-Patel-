from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('',views.index, name='index'),
    path('pay/', start_payment, name="payment"),
    path('payment/success/', handle_payment_success, name="payment_success")
]
