__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from peewee import *
db = SqliteDatabase('betsy.db')

def search(term):
    return Product.select().where(
        (Product.name ** f'%{term}%') | (Product.description ** f'%{term}%')
    ).order_by(Product.name)


def list_user_products(user_id):
    return user.products



def list_products_per_tag(tag_id):
    return tag.products


def add_product_to_catalog(user_id, product):
    product = Product.create(user=user, name=name, description=description, price=price, quantity=quantity)
    if tags:
        for tag in tags:
            try:
                product_tag = ProductTag.create(product=product, tag=Tag.create(name=tag))
            except IntegrityError:
                product_tag = ProductTag.get(product=product, tag=Tag.get(name=tag))
    return product


def update_stock(product_id, new_quantity):
    product.quantity = quantity
    product.save()


def purchase_product(product_id, buyer_id, quantity):
    if product.quantity < quantity:
        raise ValueError('Not enough stock')
    with db.atomic():
        transaction = Transaction.create(buyer=buyer, product=product, quantity=quantity)
        product.quantity -= quantity
        product.save()
    return transaction


def remove_product(product_id):
    product.delete_instance()

def populate_test_database():
    with db.atomic():
        # Create users
        alice = User.create(name='Alice', address='123 Main St', billing_info='...')
        bob = User.create(name='Bob', address='456 Elm St', billing_info='...')
        
        # Create products
        sweater = Product.create(user=alice, name='Sweater', description='A warm sweater', price=50.00, quantity=10)
        mug = Product.create(user=bob, name='Mug', description='A coffee mug', price=10.00, quantity=20

