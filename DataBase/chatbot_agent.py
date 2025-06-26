#!/usr/bin/env python3

import tkinter as tk
from tkinter import scrolledtext
import datetime
import requests
import unicodedata

CITY = "Manta,EC"  # Cambia la ciudad que quieras

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

def responder(entrada_usuario):
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
        return ("La Inteligencia Artificial (IA) es un campo de la informática "
                "que se enfoca en desarrollar sistemas capaces de realizar tareas que normalmente "
                "requieren inteligencia humana, como el aprendizaje, el razonamiento y la "
                "percepción. La IA utiliza algoritmos y modelos matemáticos para procesar "
                "grandes cantidades de datos y tomar decisiones basadas en patrones y reglas, "
                "a menudo a través del aprendizaje automático.")
    elif entrada_usuario == "quien eres":
        return "Soy un chatbot AI hecho para una práctica en clases."
    elif entrada_usuario == "ayuda":
        return ("Puedes hacerme preguntas sobre IA o sobre mi creador. Puedes escribir 'Preguntas' para ver las opciones.")
    elif entrada_usuario == "como estas":
        return "Soy un programa, ¡pero estoy funcionando perfectamente! Gracias por preguntar."
    elif entrada_usuario == "quien te creo":
        return "Fui creado por un JOSUE BRAVO, un estudiante de 8vo Nivel de la carrera de TI."
    elif entrada_usuario == "que juego le gusta a tu creador":
        return "Le gusta Genshin Impact, Zenless Zone Zero y Cult of the Lamb."
    elif entrada_usuario == "que es genshin impact":
        return ("Genshin Impact es un juego de rol de acción de 2020 producido por MiHoYo/HoYoverse. "
                "El juego presenta un mundo abierto de estilo anime y un sistema de combate basado en la "
                "acción que utiliza magia elemental y cambio de personajes. Es un juego gratuito monetizado "
                "mediante mecánicas gacha, actualizado periódicamente bajo un modelo de juegos como servicio. "
                "Se lanzó originalmente para Android, iOS, PlayStation 4 y Windows, seguido de PlayStation 5 "
                "en 2021, con una versión para Xbox Series X/S en noviembre de 2024.")
    elif entrada_usuario == "preguntas":
        return ("Aquí están las preguntas predefinidas:\n"
                " - Que es ia\n"
                " - Quien eres\n"
                " - Como estas\n"
                " - Quien te creo\n"
                " - Hora\n"
                " - Fecha\n"
                " - Clima\n"
                " - Que juego le gusta a tu creador\n"
                " - Que es genshin impact\n"
                " - Que es zenless zone zero\n"
                " - Que es cult of the lamb\n"
                " - Que es arte\n"
                " - Que es danza\n"
                " - Que es electroswing\n"
                " - Por que es importante el ingles\n"
                " - Que sabes sobre los gatos")
    elif entrada_usuario == "que es zenless zone zero":
        return ("Zenless Zone Zero es un videojuego de rol de acción de fantasía urbana desarrollado por miHoYo, "
                "publicado por miHoYo en China continental y en todo el mundo por HoYoverse para las plataformas Android, "
                "iOS, Microsoft Windows y PlayStation 5. Se lanzó el 4 de julio de 2024. Actualmente se está desarrollando "
                "un puerto para Xbox Series X|S.")
    elif entrada_usuario == "que es cult of the lamb":
        return ("Cult of the Lamb es un juego de acción y aventuras y de mazmorras desarrollado por "
                "el desarrollador independiente Massive Monster y publicado por Devolver Digital. "
                "El juego se lanzó el 11 de agosto de 2022 para Windows, Nintendo Switch, PlayStation 4, "
                "PlayStation 5, Xbox One y Xbox Series X/S. En el juego, un cordero es salvado de la muerte "
                "por una deidad extraña llamada 'El Que Espera', y debe pagar su deuda creando seguidores leales "
                "en su nombre mientras realiza una serie de cruzadas contra sus ejecutores.")
    elif entrada_usuario == "que es arte":
        return ("El arte es una forma de expresión humana que utiliza diferentes medios como la pintura, "
                "la escultura, la música, la danza y otras disciplinas para comunicar ideas, emociones y experiencias.")
    elif entrada_usuario == "que es danza":
        return ("La danza es una manifestación artística y cultural que consiste en el movimiento corporal "
                "ritmado, generalmente acompañado de música, y que expresa emociones o cuenta historias.")
    elif entrada_usuario == "que es electroswing":
        return ("El electroswing es un género musical que mezcla elementos del jazz y swing tradicional "
                "con música electrónica moderna, creando un sonido bailable y retro a la vez.")
    elif entrada_usuario == "por que es importante el ingles":
        return ("El inglés es importante porque es un idioma global usado en los negocios, la ciencia, la tecnología "
                "y la comunicación internacional, facilitando el acceso a información y oportunidades.")
    elif entrada_usuario == "que sabes sobre los gatos":
        return ("Los gatos son animales domésticos populares conocidos por su independencia, agilidad y capacidad "
                "de cazar pequeños animales. Son compañeros cariñosos y tienen una gran variedad de razas y características.")
    elif entrada_usuario == "adios":
        return "¡Adiós! Que tengas un excelente día."
    else:
        return ("Lo siento, no entendí eso. Por favor intenta con otra pregunta o escribe 'Ayuda'. "
                "Para desplegar las opciones que puedes preguntar escribe 'Preguntas'.")

def enviar_mensaje():
    entrada = entry.get()
    if entrada.strip() == "":
        return
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, f"Tú: {entrada}\n")
    
    respuesta = responder(entrada)
    text_area.insert(tk.END, f"Chatbot: {respuesta}\n\n")
    text_area.config(state=tk.DISABLED)
    text_area.see(tk.END)
    entry.delete(0, tk.END)
    
    if quitar_tildes(entrada.strip().lower()) == "adios":
        root.after(1500, root.destroy)  # Cierra la ventana después de 1.5 segundos

# Configuración de la ventana principal
root = tk.Tk()
root.title("Chatbot AI")
root.geometry("600x400")

# Área de texto para mostrar la conversación con scroll
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Mostrar mensajes iniciales
text_area.config(state=tk.NORMAL)
text_area.insert(tk.END, "Bienvenido al chat\n")
text_area.insert(tk.END, "Chatbot: ¡Hola! Soy tu chatbot AI sencillo.\n\n")
text_area.config(state=tk.DISABLED)

# Entrada de texto para el usuario
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=(0,10), fill=tk.X)
entry.focus()

# Botón para enviar mensaje
send_button = tk.Button(root, text="Enviar", command=enviar_mensaje)
send_button.pack(padx=10, pady=(0,10))

# Enviar mensaje al presionar Enter
root.bind('<Return>', lambda event: enviar_mensaje())

root.mainloop()
