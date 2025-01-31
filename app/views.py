from django.shortcuts import render
from django.http import JsonResponse
from . models import Product,Order
from django.db import transaction

def book_products(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('product_ids')
        customer = request.POST.get('customer')
        quantity = int(request.POST.get('quantity',1))

        try:
            
            ##atomic transaction##
            with transaction.atomic():
                products = Product.objects.filter(
                    id__in = product_ids
                ).select_for_update()

                for product in products:
                    if product.stock < quantity:
                        return JsonResponse({
                            'error':f'Product {product.name} has insufficient stock.'
                        },status=400)
                    
                order = Order.objects.create(
                    customer = customer,
                    quantity = quantity
                )
                order.products.set(products)

                for product in products:
                    product.stock -= quantity
                    product.save()

                order.confirmed = True
                order.save()

                return JsonResponse({
                    'message':'Order confirmed successfully!'
                })
        except Exception as e:
            return JsonResponse({'error':str(e)},status=500)
                
            

