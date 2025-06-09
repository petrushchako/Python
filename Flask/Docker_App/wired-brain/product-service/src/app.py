from flask import Flask, jsonify, request

products = [
    {"id": 1, "name": "Product 1"},
    {"id": 2, "name": "Product 2"}
]

app = Flask(__name__)

# curl -v http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# curl -v http://localhost:5000/products/1
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product_list = [product for product in products if product['id']== id]
    if len(product_list)==0:
        return f'Product with id {id} not found', 404
    return jsonify(product_list[0])