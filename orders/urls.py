from django.urls import path
from .views import MyorderView

urlpatterns = [
    path('mi-orden', MyorderView.as_view(), name="my_order")
]