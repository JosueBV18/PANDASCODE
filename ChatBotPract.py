#!/usr/bin/env python3

import datetime
import requests
import unicodedata
import tkinter as tk
from tkinter import scrolledtext

CITY = "Manta,EC"

def quitar_tildes(cadena):
    return ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def obtener_hora():
    ahora = datetime.datetime.now()
    return ahora.strftime("%H:%M:%S")

def obtener_fecha():
    hoy = datetime.datetime.now()
    return hoy.strftime("%d/%m/%Y")

def obtener_clima():
    try:
        url = f"https://wttr.in/{CITY}?format=3"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            return "No pude obtener el clima ahora."
    except Exception as e:
        return f"Error al obtener el clima: {str(e)}"

def responder_entrada(entrada_usuario):
    entrada_usuario = quitar_tildes(entrada_usuario.strip())
    if entrada_usuario == "hola":
        return "¡Hola! ¿En qué puedo ayudarte hoy?"
    elif entrada_usuario == "hora":
        return f"La hora actual es {obtener_hora()}."
    elif entrada_usuario == "fecha":
        return f"La fecha de hoy es {obtener_fecha()}."
    elif entrada_usuario == "clima":
        return obtener_clima()
    elif entrada_usuario == "que es ia":
        return ("La Inteligencia Artificial (IA) es un campo de la informática que se enfoca "
                "en desarrollar sistemas capaces de realizar tareas que normalmente requieren "
                "inteligencia humana, como el aprendizaje, el razonamiento y la percepción.")
    elif entrada_usuario == "quien eres":
        return "Soy un chatbot AI hecho para una práctica en clases."
    elif entrada_usuario == "ayuda":
        return "Puedes hacerme preguntas sobre IA, clima, hora, fecha, o sobre mi creador. Escribe 'Preguntas' para ver opciones."
    elif entrada_usuario == "como estas":
        return "Soy un programa, ¡pero estoy funcionando perfectamente! Gracias por preguntar."
    elif entrada_usuario == "quien te creo":
        return "Fui creado por Josue Bravo, estudiante de 8vo nivel de la carrera de TI."
    elif entrada_usuario == "que juego le gusta a tu creador":
        return "Le gusta Genshin Impact, Zenless Zone Zero y Cult of the Lamb."
    elif entrada_usuario == "que es genshin impact":
        return ("Genshin Impact es un juego de rol de acción de 2020 producido por MiHoYo/HoYoverse. "
                "Presenta un mundo abierto de estilo anime y un sistema de combate basado en magia elemental.")
    elif entrada_usuario == "preguntas":
        return ("Preguntas que puedes hacer:\n- Que es ia\n- Quien eres\n- Como estas\n- Quien te creo\n"
                "- Hora\n- Fecha\n- Clima\n- Que juego le gusta a tu creador\n- Que es genshin impact\n"
                "- Que es zenless zone zero\n- Que es cult of the lamb\n- Que es arte\n- Que es danza\n"
                "- Que es electroswing\n- Por que es importante el ingles\n- Que sabes sobre los gatos")
    elif entrada_usuario == "que es zenless zone zero":
        return ("Zenless Zone Zero es un videojuego de rol de acción de fantasía urbana desarrollado por miHoYo. "
                "Se lanzó el 4 de julio de 2024.")
    elif entrada_usuario == "que es cult of the lamb":
        return ("Cult of the Lamb es un juego de acción y aventuras desarrollado por Massive Monster y publicado por Devolver Digital.")
    elif entrada_usuario == "que es arte":
        return ("El arte es una forma de expresión humana que utiliza diferentes medios como la pintura, la escultura, "
                "la música, la danza y otras disciplinas para comunicar ideas, emociones y experiencias.")
    elif entrada_usuario == "que es danza":
        return ("La danza es una manifestación artística y cultural que consiste en el movimiento corporal ritmado, "
                "generalmente acompañado de música, y que expresa emociones o cuenta historias.")
    elif entrada_usuario == "que es electroswing":
        return ("El electroswing es un género musical que mezcla jazz y swing tradicional con música electrónica moderna, "
                "creando un sonido bailable y retro.")
    elif entrada_usuario == "por que es importante el ingles":
        return ("El inglés es importante porque es un idioma global usado en negocios, ciencia, tecnología y comunicación internacional.")
    elif entrada_usuario == "que sabes sobre los gatos":
        return ("Los gatos son animales domésticos conocidos por su independencia, agilidad y capacidad de caza. Son compañeros cariñosos.")
    elif entrada_usuario == "adios":
        return "¡Adiós! Que tengas un excelente día."
    else:
        return "Lo siento, no entendí eso. Por favor intenta con otra pregunta o escribe 'Ayuda'."

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot AI")

# Crear el área de texto para mostrar la conversación
texto_conversacion = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=60, height=20, state='disabled')
texto_conversacion.pack(padx=10, pady=10)

# Crear la caja de texto para escribir la pregunta
entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack(padx=10, pady=(0,10))
entrada_texto.focus()

def enviar_mensaje(event=None):
    mensaje_usuario = entrada_texto.get()
    if mensaje_usuario.strip() == "":
        return
    # Mostrar mensaje usuario
    texto_conversacion.config(state='normal')
    texto_conversacion.insert(tk.END, "Tú: " + mensaje_usuario + "\n")
    texto_conversacion.config(state='disabled')
    entrada_texto.delete(0, tk.END)

    # Obtener respuesta y mostrarla
    respuesta = responder_entrada(mensaje_usuario)
    texto_conversacion.config(state='normal')
    texto_conversacion.insert(tk.END, "Chatbot: " + respuesta + "\n\n")
    texto_conversacion.config(state='disabled')
    texto_conversacion.see(tk.END)

    # Si el usuario dice adios, cerramos ventana
    if respuesta.startswith("¡Adiós!"):
        ventana.after(1500, ventana.destroy)

# Botón para enviar mensaje
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=(0,10))

# Permitir enviar mensaje al presionar Enter
ventana.bind('<Return>', enviar_mensaje)

ventana.mainloop()
