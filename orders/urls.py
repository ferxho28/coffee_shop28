from django.urls import path
from .views import MyorderView, CreateOrderProductView

urlpatterns = [
    path('mi-orden', MyorderView.as_view(), name="my_order"),
    path('agregar-producto', CreateOrderProductView.as_view(), name="add_product")
]