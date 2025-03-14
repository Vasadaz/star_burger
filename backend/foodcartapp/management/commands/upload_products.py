import json

from django.core.management.base import BaseCommand

from backend.foodcartapp.models import Product, ProductCategory, Restaurant, RestaurantMenuItem


class Command(BaseCommand):
    help = 'Start adding products'

    def handle(self, *args, **options):

        with open(options['path'], 'r', encoding='utf-8') as file:
            products = json.load(file)

        for product in products:
            self.add_product(product)

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            nargs='?',
            type=str,
        )

    @staticmethod
    def add_category(category: str) -> ProductCategory:
        if category:
            category_obj, created = ProductCategory.objects.get_or_create(
                name=category,
            )
            return category_obj

    @staticmethod
    def add_product_to_menu(product: Product):
        restaurants = Restaurant.objects.all()

        for restaurant in restaurants:
            menu_product, created = RestaurantMenuItem.objects.get_or_create(
                restaurant=restaurant,
                product=product,
            )

    def add_product(self, product_notes: dict):
        product, created = Product.objects.get_or_create(
            name=product_notes['title'],
            price=product_notes['price'],
            image=product_notes['img'],
            defaults={
                'category': self.add_category(product_notes.get('type')),
                'description': product_notes.get('description', ''),
                'special_status': product_notes.get('special_status', False),
            }
        )

        self.add_product_to_menu(product)

        if created:
            self.stdout.write(f'Added product "{product}".')
        else:
            self.stdout.write(f'\033[93mDOUBLE:\033[0m product "{product}" already exists!')
