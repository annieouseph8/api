from django.shortcuts import render

from django.http import JsonResponse
from .models import Product

def get_product_data(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        data = {
            'product_id': product.id,
            'name': product.name,
            'availability': product.availability
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
