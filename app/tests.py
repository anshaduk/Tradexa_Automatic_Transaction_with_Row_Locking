from django.test import TestCase
from django.test import Client
from . models import Product
import threading

class ConcurrencyTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name = 'Test Product',stock=5)
        self.client = Client()

    def test_concurrent_orders(self):
        def book_order():
            response = self.client.post('/book/',{
                'product_ids' : [self.product.id],
                'customer' : 'Customer A',
                'quantity' : 4
            })
            return response
        
        thread1 = threading.Thread(target=book_order)
        thread1.start()

        thread2 = threading.Thread(target=book_order)
        thread2.start()

        thread1.join()
        thread2.join()

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock,1)

