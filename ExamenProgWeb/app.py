from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def home():
    return render_template('menu.html')

# Ruta para Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        cans = int(request.form['cans'])
        total = cans * 9000
        discount = 0
        if 18 <= age <= 30:
            discount = 0.15
        elif age > 30:
            discount = 0.25
        discount_amount = total * discount
        final_price = total - discount_amount
        return render_template(
            'form1.html',
            result=True,
            name=name,
            total=total,
            discount_amount=discount_amount,
            final_price=final_price
        )
    return render_template('form1.html', result=False)

# Ruta para Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    users = {'juan': 'admin', 'pepe': 'user'}
    message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            if username == 'juan':
                message = f"Bienvenido Administrador {username}"
            else:
                message = f"Bienvenido Usuario {username}"
        else:
            message = "Usuario o contraseña incorrectos"

    return render_template('form2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
