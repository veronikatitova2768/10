from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список товаров
products = []

@app.route('/')
def index():
    return redirect(url_for('show_products'))

@app.route('/products')
def show_products():
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        quantity = request.form.get('quantity')
        if product_name and quantity:
            products.append({'name': product_name, 'quantity': quantity})
        return redirect(url_for('show_products'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
