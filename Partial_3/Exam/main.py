# # main.py
# from datetime import datetime
# from Voice.speech_to_text import listen
from Voice.text_to_speech import speak
# from LDA.lda_model import execute_lda
# from Historia.story_generator import generar_historia

# def saludo(nombre):
#     hora = datetime.now().hour
#     if hora < 12:
#         saludo = "Buenos días"
#     elif hora < 18:
#         saludo = "Buenas tardes"
#     else:
#         saludo = "Buenas noches"

#     hablar(f"{saludo}, {nombre}")

# def menu():
#     hablar("Elige una opción. A: Asignación latente. B: Historia. C: Resumen")
#     opcion = escuchar().lower()
#     return opcion

# def main():
#     hablar("Hola, soy Aletza. Dime tu nombre")
#     nombre = escuchar()
#     saludo(nombre)

#     opcion = menu()

#     if "a" in opcion:
#         ejecutar_lda()
#     elif "b" in opcion:
#         generar_historia()
#     elif "c" in opcion:
#         hablar("Resumen con LDA aún en desarrollo")
#     else:
#         hablar("Opción no válida")

# if __name__ == "__main__":
#     main()

speak("Hola, soy Aletza, tu asistente virtual.")