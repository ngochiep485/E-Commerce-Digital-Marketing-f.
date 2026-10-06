from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Load product data from JSON file
DATA_FILE = os.path.join(app.root_path, '..', 'products.json')

def load_products():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

products = load_products()

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('product.html', product=product)

# API endpoint for price comparison data (JSON)
@app.route('/api/compare/<int:product_id>')
def api_compare(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    # In a real app, prices would be fetched from external APIs.
    # Here we just return the stored vendor prices.
    return jsonify({'product': product['name'], 'prices': product['prices']})

if __name__ == '__main__':
    # Enable debug mode for beginners
    app.run(debug=True, host='0.0.0.0', port=5000)
