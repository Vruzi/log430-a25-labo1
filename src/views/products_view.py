"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the Product """
        controller = ProductController()
        # continue code here
        while True:
            print("\n1. Montrer la liste des produits\n2. Ajouter un nouveau produit\n3. Supprimer un produit\n4. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_user(product)
            elif choice == '3': # optionel par Samuel Rondeau
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.delete_product(product)
            elif choice == '4':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{product.id}: {product.name} : {product.price} ({product.brand})" for product in products))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new user """
        name = input("Nom d'utilisateur : ").strip()
        brand = input("Adresse courriel : ").strip()
        price = float(input("Prix : ").strip())
        return name, brand, price