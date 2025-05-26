#!/usr/bin/env python3

import datetime
import requests
import unicodedata
import tkinter as tk
from tkinter import scrolledtext

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

def responder_a_usuario(entrada_usuario):
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
        return ("La Inteligencia Artificial (IA) es un campo de la informática que se enfoca en desarrollar sistemas "
                "capaces de realizar tareas que normalmente requieren inteligencia humana, como el aprendizaje, el razonamiento "
                "y la percepción. La IA utiliza algoritmos y modelos matemáticos para procesar grandes cantidades de datos y "
                "tomar decisiones basadas en patrones y reglas, a menudo a través del aprendizaje automático.")
    elif entrada_usuario == "quien eres":
        return "Soy un chatbot AI hecho para una práctica en clases."
    elif entrada_usuario == "ayuda":
        return "Puedes hacerme preguntas sobre IA o sobre mi creador. Puedes escribir 'Preguntas' para que te dé las que ya existen."
    elif entrada_usuario == "como estas":
        return "Soy un programa, ¡pero estoy funcionando perfectamente! Gracias por preguntar."
    elif entrada_usuario == "quien te creo":
        return "Fui creado por un JOSUE BRAVO, un estudiante de 8vo Nivel de la carrera de TI."
    elif entrada_usuario == "que juego le gusta a tu creador":
        return "Le gusta Genshin Impact, Zenless Zone Zero y Cult of the Lamb."
    elif entrada_usuario == "que es genshin impact":
        return ("Genshin Impact es un juego de rol de acción de 2020 producido por MiHoYo/HoYoverse. "
                "El juego presenta un mundo abierto de estilo anime y un sistema de combate basado en la acción "
                "que utiliza magia elemental y cambio de personajes. Es un juego gratuito monetizado mediante "
                "mecánicas gacha, actualizado periódicamente bajo un modelo de juegos como servicio.")
    elif entrada_usuario == "preguntas":
        return ("Aquí están las preguntas predefinidas:\n"
                " - Que es ia\n - Quien eres\n - Como estas\n - Quien te creo\n - Hora\n - Fecha\n - Clima\n"
                " - Que juego le gusta a tu creador\n - Que es genshin impact\n - Que es zenless zone zero\n"
                " - Que es cult of the lamb\n - Que es arte\n - Que es danza\n - Que es electroswing\n"
                " - Por que es importante el ingles\n - Que sabes sobre los gatos")
    elif entrada_usuario == "que es zenless zone zero":
        return ("Zenless Zone Zero es un videojuego de rol de acción de fantasía urbana desarrollado por miHoYo, "
                "publicado en China continental y en todo el mundo para varias plataformas. Se lanzó el 4 de julio de 2024.")
    elif entrada_usuario == "que es cult of the lamb":
        return ("Cult of the Lamb es un juego de acción y aventuras desarrollado por Massive Monster y publicado por Devolver Digital. "
                "Se lanzó en 2022 para múltiples plataformas.")
    elif entrada_usuario == "que es arte":
        return ("El arte es una forma de expresión humana que utiliza diferentes medios como la pintura, la escultura, la música, "
                "la danza y otras disciplinas para comunicar ideas, emociones y experiencias.")
    elif entrada_usuario == "que es danza":
        return ("La danza es una manifestación artística y cultural que consiste en el movimiento corporal ritmado, "
                "generalmente acompañado de música, y que expresa emociones o cuenta historias.")
    elif entrada_usuario == "que es electroswing":
        return ("El electroswing es un género musical que mezcla elementos del jazz y swing tradicional con música electrónica moderna, "
                "creando un sonido bailable y retro a la vez.")
    elif entrada_usuario == "por que es importante el ingles":
        return ("El inglés es importante porque es un idioma global usado en los negocios, la ciencia, la tecnología y la comunicación "
                "internacional, facilitando el acceso a información y oportunidades.")
    elif entrada_usuario == "que sabes sobre los gatos":
        return ("Los gatos son animales domésticos populares conocidos por su independencia, agilidad y capacidad de cazar pequeños animales. "
                "Son compañeros cariñosos y tienen una gran variedad de razas y características.")
    elif entrada_usuario == "adios":
        return "¡Adiós! Que tengas un excelente día."
    else:
        return ("Lo siento, no entendí eso. Por favor intenta con otra pregunta o escribe 'Ayuda'. "
                "Para desplegar las opciones que puedes preguntar escribe 'Preguntas'.")

# ----- INTERFAZ GRÁFICA CON TKINTER -----

def enviar_mensaje():
    entrada = entrada_usuario.get()
    if entrada.strip() == "":
        return
    
    # Mostrar mensaje del usuario en el cuadro de texto
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "Tú: " + entrada + "\n")
    
    respuesta = responder_a_usuario(entrada)
    
    chat_text.insert(tk.END, "Chatbot: " + respuesta + "\n\n")
    chat_text.config(state=tk.DISABLED)
    chat_text.see(tk.END)
    
    if quitar_tildes(entrada.strip()) == "adios":
        ventana.after(2000, ventana.destroy)
    
    entrada_usuario.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Chatbot AI Sencillo")
ventana.geometry("600x500")

# Área de texto para conversación
chat_text = scrolledtext.ScrolledText(ventana, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12))
chat_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entrada de texto para usuario
entrada_usuario = tk.Entry(ventana, font=("Arial", 14))
entrada_usuario.pack(padx=10, pady=10, fill=tk.X)
entrada_usuario.focus()

# Botón para enviar mensaje
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje, font=("Arial", 12))
boton_enviar.pack(pady=5)

# Permitir enviar mensaje con tecla Enter
ventana.bind('<Return>', lambda event: enviar_mensaje())

# Mensaje de bienvenida inicial
chat_text.config(state=tk.NORMAL)
chat_text.insert(tk.END, "Chatbot: ¡Hola! Soy tu chatbot AI sencillo. ¿En qué puedo ayudarte hoy?\n\n")
chat_text.config(state=tk.DISABLED)

ventana.mainloop()
