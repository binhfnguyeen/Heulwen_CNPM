import json
from saleapp.app.models import Category, Product

def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None):
    # with open("data/products.json", "r") as file:
    #     data = json.load(file)
    #     return data
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id == cate_id)

    return query.all()