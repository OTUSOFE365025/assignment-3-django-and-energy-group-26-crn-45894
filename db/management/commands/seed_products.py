from django.core.management.base import BaseCommand
from db.models import Product


class Command(BaseCommand):
    help = 'Seed the DB with sample products'

    def handle(self, *args, **options):
        # Short, easy-to-type product codes for TA/demo use
        sample = [
            ("1001", "Apple iPhone 15", "999.99"),
            ("1002", "Samsung Galaxy S24", "899.99"),
            ("1003", "Wireless Earbuds", "149.99"),
            ("1004", "USB-C Cable", "19.99"),
            ("1005", "Phone Case", "29.99"),
            ("1006", "Screen Protector", "14.99"),
            ("1007", "Portable Charger", "39.99"),
            ("1008", "Bluetooth Speaker", "79.99"),
            ("1009", "Smart Watch", "299.99"),
            ("1010", "Laptop Stand", "49.99"),
        ]

        for upc, name, price in sample:
            Product.objects.update_or_create(upc=upc, defaults={"name": name, "price": price})

        self.stdout.write(self.style.SUCCESS('Seeded sample products.'))
