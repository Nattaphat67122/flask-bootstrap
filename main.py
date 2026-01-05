from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cars =[
    { 'id': 1, 'brand': 'Toyota', 'model': 'Yaris Ativ', 'year': 2020 , 'price': 559000},
    { 'id': 2, 'brand': 'Honda', 'model': 'City Hatchback', 'year': 2024 , 'price': 650000},
    { 'id': 3, 'brand': 'Nissan', 'model': 'Amera', 'year': 2025 , 'price': 450000}
]

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/cars')
def all_car():
    return render_template('cars/cars.html',
                           title='Show All Car Page',
                            cars=cars)

@app.route('/car/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = int(request.form['year'])
        price = int(request.form['price'])

        length = len(cars)
        id = cars[length - 1]['id'] + 1

        car = { 'id': id, 'brand': brand, 'model': model, 'year': year , 'price': price}
        cars.append(car)

    return render_template('cars/new_car.html',
                           title='New Car Page')