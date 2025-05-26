#!/usr/bin/env python3

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


print('BIENVENIDO AL CHAT')

def chatbot():
    print("Chatbot: ¡Hola! Soy tu chatbot AI sencillo.")
    
    while True:
        entrada_usuario = input("Tú: ").strip()
        entrada_usuario = quitar_tildes(entrada_usuario)

        if entrada_usuario == "hola":
            print("Chatbot: ¡Hola! ¿En qué puedo ayudarte hoy?")
        elif entrada_usuario == "hora":
            print(f"Chatbot: La hora actual es {obtener_hora()}.")
        elif entrada_usuario == "fecha":
            print(f"Chatbot: La fecha de hoy es {obtener_fecha()}.")
        elif entrada_usuario == "clima":
            print(f"Chatbot: {obtener_clima()}")
        elif entrada_usuario == "que es ia":
            print("Chatbot: La Inteligencia Artificial (IA) es un campo de la informática " \
                  "que se enfoca en desarrollar sistemas capaces de realizar tareas que normalmente " \
                  "requieren inteligencia humana, como el aprendizaje, el razonamiento y la " \
                  "percepción. La IA utiliza algoritmos y modelos matemáticos para procesar " \
                  "grandes cantidades de datos y tomar decisiones basadas en patrones y reglas, " \
                  "a menudo a través del aprendizaje automático.")
        elif entrada_usuario == "quien eres":
            print("Chatbot: Soy un chatbot AI hecho para una práctica en clases.")
        elif entrada_usuario == "ayuda":
            print("Chatbot: Puedes hacerme preguntas sobre IA o sobre mi creador. Puedes escribir 'Preguntas' para que te dé la que ya existen")
        elif entrada_usuario == "como estas":
            print("Chatbot: Soy un programa, ¡pero estoy funcionando perfectamente! Gracias por preguntar")
        elif entrada_usuario == "quien te creo":
            print("Chatbot: Fui creado por un JOSUE BRAVO, un estudiante de 8vo Nivel de la carrera de TI.")
        elif entrada_usuario == "que juego le gusta a tu creador":
            print("Chatbot: Le gusta Genshin Impact, Zenless Zone Zero y Cult of the Lamb.")
        elif entrada_usuario == "que es genshin impact":
            print("Chatbot: Genshin Impact es un juego de rol de acción de 2020 producido por MiHoYo/HoYoverse. "
                  "El juego presenta un mundo abierto de estilo anime y un sistema de combate basado en la "
                  "acción que utiliza magia elemental y cambio de personajes. Es un juego gratuito monetizado "
                  "mediante mecánicas gacha, actualizado periódicamente bajo un modelo de juegos como servicio. "
                  "Se lanzó originalmente para Android, iOS, PlayStation 4 y Windows, seguido de PlayStation 5 "
                  "en 2021, con una versión para Xbox Series X/S en noviembre de 2024.")
        elif entrada_usuario == "preguntas":
            print("Chatbot: Aquí están las preguntas predefinidas:")
            print(" - Que es ia")
            print(" - Quien eres")
            print(" - Como estas")
            print(" - Quien te creo")
            print(" - Hora")
            print(" - Fecha")
            print(" - Clima")
            print(" - Que juego le gusta a tu creador")
            print(" - Que es genshin impact")
            print(" - Que es zenless zone zero")
            print(" - Que es cult of the lamb")
            print(" - Que es arte")
            print(" - Que es danza")
            print(" - Que es electroswing")
            print(" - Por que es importante el ingles")
            print(" - Que sabes sobre los gatos")
        elif entrada_usuario == "que es zenless zone zero":
            print("Chatbot: Zenless Zone Zero es un videojuego de rol de acción de fantasía urbana desarrollado por miHoYo, "
                  "publicado por miHoYo en China continental y en todo el mundo por HoYoverse para las plataformas Android, "
                  "iOS, Microsoft Windows y PlayStation 5. Se lanzó el 4 de julio de 2024. Actualmente se está desarrollando "
                  "un puerto para Xbox Series X|S.")
        elif entrada_usuario == "que es cult of the lamb":
            print("Chatbot: Cult of the Lamb es un juego de acción y aventuras y de mazmorras desarrollado por "
                  "el desarrollador independiente Massive Monster y publicado por Devolver Digital. "
                  "El juego se lanzó el 11 de agosto de 2022 para Windows, Nintendo Switch, PlayStation 4, "
                  "PlayStation 5, Xbox One y Xbox Series X/S. En el juego, un cordero es salvado de la muerte "
                  "por una deidad extraña llamada 'El Que Espera', y debe pagar su deuda creando seguidores leales "
                  "en su nombre mientras realiza una serie de cruzadas contra sus ejecutores.")
        # NUEVAS PREGUNTAS SOBRE ARTE, DANZA, ELECTROSWING, INGLES Y GATOS
        elif entrada_usuario == "que es arte":
            print("Chatbot: El arte es una forma de expresión humana que utiliza diferentes medios como la pintura, "
                  "la escultura, la música, la danza y otras disciplinas para comunicar ideas, emociones y experiencias.")
        elif entrada_usuario == "que es danza":
            print("Chatbot: La danza es una manifestación artística y cultural que consiste en el movimiento corporal "
                  "ritmado, generalmente acompañado de música, y que expresa emociones o cuenta historias.")
        elif entrada_usuario == "que es electroswing":
            print("Chatbot: El electroswing es un género musical que mezcla elementos del jazz y swing tradicional "
                  "con música electrónica moderna, creando un sonido bailable y retro a la vez.")
        elif entrada_usuario == "por que es importante el ingles":
            print("Chatbot: El inglés es importante porque es un idioma global usado en los negocios, la ciencia, la tecnología "
                  "y la comunicación internacional, facilitando el acceso a información y oportunidades.")
        elif entrada_usuario == "que sabes sobre los gatos":
            print("Chatbot: Los gatos son animales domésticos populares conocidos por su independencia, agilidad y capacidad "
                  "de cazar pequeños animales. Son compañeros cariñosos y tienen una gran variedad de razas y características.")
        elif entrada_usuario == "adios":
            print("Chatbot: ¡Adiós! Que tengas un excelente día.")
            break
        else:
            print("Chatbot: Lo siento, no entendí eso. Por favor intenta con otra pregunta o escribe 'Ayuda'. " \
                  "Para desplegar las opciones que puedes preguntar escribe 'Preguntas'")

if __name__ == "__main__":
    chatbot()
