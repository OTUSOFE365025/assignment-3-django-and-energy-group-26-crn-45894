############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Django’s autoreloader runs this script twice (watcher and worker). Guard against
# double-seeding/printing so the console output stays tidy.
RUNNING_IN_AUTORELOADER = os.environ.get('RUN_MAIN') == 'true'

if not RUNNING_IN_AUTORELOADER:
    # Seed a few users in the database (if missing)
    if User.objects.count() == 0:
        User.objects.create(name='Dan')
        User.objects.create(name='Robert')

    for u in User.objects.all():
        print(f'ID: {u.id} \tUsername: {u.name}')

    # Sample products
    from db.models import Product

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

    # Check if UPC code exists
    for upc, name, price in sample:
        Product.objects.update_or_create(upc=upc, defaults={"name": name, "price": price})
    print("Ensured demo short-code products are present.")

    # Start the Django development server so the TA can open the UI and scan items
    print('\nStarting Django development server at http://127.0.0.1:8000/ — press CTRL+C to stop')

from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])
