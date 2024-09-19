from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from .forms import ProductForm
from .serializer import ProductSeralizer

class ProductFromView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = 'products'

class ProductListAPI(APIView):
    authentication_classes = []  #permisos para acceder añ API
    permission_classes = []

    def get(self, request): #esta Func trae los objetos del modelo productoos ,  
        products = Product.objects.all()
        serializer = ProductSeralizer(products, many=True) #seguido los serializa en una lista
        return Response(serializer.data) #Los devuelve en formato json
        