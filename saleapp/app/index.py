from flask import render_template, request
import dao
from saleapp.app import app


@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')
    products= dao.load_products(cate_id=cate_id)
    return render_template("index.html", categories=cates, products=products)


if __name__ == '__main__':
    app.run(debug=True)
