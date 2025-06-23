#!/usr/bin/env python3

import flask 
from flask import Flask, render_template, request, redirect, url_for, session
import json

#versionflask = flask.__version__
#print(versionflask)

print('Class 02 FLASK')
print('-----------------------------------------------------------------------------------------', '\n')

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta_aqui'

@app.route("/")
def index():
    return "Hello, flask"

@app.route("/about")
def about():
    return "Thist a WebPage ABOUT, flask"

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/pageName")
def pageName():
    return render_template('hello.html', nameHTML='Josue Bravo')

@app.route('/sumar')
def sumar():
    # Obtener parámetros 'a' y 'b' de la URL, con valor por defecto 0
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)
    
    resultado = a + b
    return f"La suma de {a} + {b} es {resultado}"

@app.route('/mostrar')
def mostrar():
    # Obtener el parámetro 'n' desde la URL, por defecto 1
    n = request.args.get('n', default=1, type=int)
    
    if n < 1:
        return "Por favor ingresa un número entero mayor o igual a 1."

    # Crear una lista con números del 1 al n
    numeros = list(range(1, n + 1))
    
    # Convertir la lista a una cadena separada por comas
    resultado = ', '.join(str(num) for num in numeros)
    
    return f"Números del 1 al {n}: {resultado}"

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre', '')
        edad = request.form.get('edad', '')
        email = request.form.get('email', '')
        domicilio = request.form.get('domicilio', '')
        historial = request.form.get('historial', '')
        referencias = request.form.get('referencias', '')

        datos_usuario = {
            'Nombre': nombre,
            'Edad': edad,
            'Email': email,
            'Domicilio': domicilio,
            'Historial de estudios': historial,
            'Referencias': referencias
        }

        # Guardar datos como JSON en session
        session['datos_json'] = json.dumps(datos_usuario, ensure_ascii=False, indent=4)

        # Redirigir a página que muestra los datos
        return redirect(url_for('resultado'))

    return render_template('datos.html')

@app.route('/resultado')
def resultado():
    datos_json_str = session.get('datos_json', '{}')
    datos_usuario = json.loads(datos_json_str)  # Convierte string JSON a dict
    return render_template('resultado.html', datos_json=datos_usuario)



if __name__ == '__main__':
    app.run(debug=True)


