from daos.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self):
        """ List all product """
        return self.dao.select_all()
    
    def delete_product(self, product): #optional by Samuel Rondeau
        """ Update the price of a product """
        product = self.dao.delete(product)

    def create_product(self, product):
        """ Create a new product based on product inputs """
        self.dao.insert(product)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()
