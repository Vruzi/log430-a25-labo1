from daos.product_dao_mongo import ProductDAOMongo
from models.product import Product

dao = ProductDAOMongo()

def test_product_select():
    products_list = dao.select_all()
    assert len(products_list) >= 3

def test_product_insert():
    product = Product(None, 'Shampoing', 'Dove', 6.99)
    dao.insert(product)
    product_list = dao.select_all()
    products_names = [p.name for p in product_list]
    assert product.name in products_names

def test_product_update():
    product = Product(None, 'Banane', 'Banana.Inc', 9.00)
    assigned_id = dao.insert(product)

    corrected_price = 10.00
    product.id = assigned_id
    product.price = corrected_price

    dao.update(product)

    products_list = dao.select_all()
    prices = [p.price for p in products_list]
    assert corrected_price in prices

def test_product_delete():
    product = Product(None, 'Chips', 'Lays', 3.50)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    products_list = dao.select_all()
    names = [p.name for p in products_list]
    assert product.name not in names