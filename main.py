from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = b'what yes'

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

        flash('Add New Car Successfully!!!', 'success')
        return redirect(url_for('all_car'))

    return render_template('cars/new_car.html',
                           title='New Car Page')

@app.route('/car/<int:id>/delete')
def delete_car(id):
    for car in cars:
       if id == car['id']:
           cars.remove(car)
           break
    flash('Delete Car Successfully!!!', 'success')
    return redirect(url_for('all_car'))

@app.route('/car/<int:id>/edit')
def edit_car(id):
   return render_template('cars/edit_car.html',
                          title='Edit Car Page')