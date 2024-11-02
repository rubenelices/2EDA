import random
import matplotlib.pyplot as plt

class Preguntas:
    def __init__(self):
        # Lista de preguntas y respuestas en forma de diccionario
        self.preguntas = [
            {
                "pregunta": "¿Cuál es la capital de Estados Unidos?",
                "opciones": ["a) Nueva York", "b) Washington D.C", "c) San Francisco", "d) Las Vegas"],
                "respuesta_correcta": "b"
            },
            {
                "pregunta": "¿Quién pintó la Mona Lisa?",
                "opciones": ["a) Vincent Van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Miguel Ángel"],
                "respuesta_correcta": "c"
            },
            {
                "pregunta": "¿Cuál es el río más largo del mundo?",
                "opciones": ["a) Amazonas", "b) Nilo", "c) Yangtsé", "d) Misisipi"],
                "respuesta_correcta": "b"
            },
            {
                "pregunta": "¿En qué año el hombre llegó a la Luna?",
                "opciones": ["a) 1965", "b) 1969", "c) 1972", "d) 1960"],
                "respuesta_correcta": "b"
            },
            {
                "pregunta": "¿Cuál es el país más grande del mundo?",
                "opciones": ["a) China", "b) Canadá", "c) Estados Unidos", "d) Rusia"],
                "respuesta_correcta": "d"
            },
            {
                "pregunta": "¿Quién escribió 'Cien años de soledad'?",
                "opciones": ["a) Mario Vargas Llosa", "b) Gabriel García Márquez", "c) Isabel Allende", "d) Jorge Luis Borges"],
                "respuesta_correcta": "b"
            },
            {
                "pregunta": "¿Cuál es el océano más grande?",
                "opciones": ["a) Atlántico", "b) Índico", "c) Pacífico", "d) Ártico"],
                "respuesta_correcta": "c"
            },
            {
                "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
                "opciones": ["a) George Washington", "b) Abraham Lincoln", "c) Thomas Jefferson", "d) John Adams"],
                "respuesta_correcta": "a"
            },
            {
                "pregunta": "¿Cuál es el país más poblado del mundo?",
                "opciones": ["a) India", "b) Estados Unidos", "c) China", "d) Indonesia"],
                "respuesta_correcta": "c"
            },
            {
                "pregunta": "¿Cuántos jugadores tiene un equipo de fútbol en el campo?",
                "opciones": ["a) 10", "b) 11", "c) 12", "d) 9"],
                "respuesta_correcta": "b"
            }
        ]
    
    # Método para hacer preguntas a los jugadores
    def hacer_preguntas(self, jugadores):
        resultados = {jugador: 0 for jugador in jugadores}  # Puntuación por jugador
        
        # Preguntamos a cada jugador por turno
        for jugador in jugadores:
            print(f"\nTurno de {jugador}:")
            random.shuffle(self.preguntas)  # Barajamos las preguntas
            for i, pregunta in enumerate(self.preguntas):
                print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
                for opcion in pregunta["opciones"]:
                    print(opcion)
                
                respuesta = input(f"{jugador}, introduce la letra de la respuesta: ").lower()
                
                if respuesta == pregunta["respuesta_correcta"]:
                    print("¡Correcto!")
                    resultados[jugador] += 1
                else:
                    print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta_correcta']}")
        
        return resultados

    # Método para mostrar los resultados finales
    def mostrar_resultados(self, resultados):
        print("\nResultados Finales:")
        for jugador, puntaje in resultados.items():
            print(f"{jugador}: {puntaje} respuestas correctas")

        # Gráfica de resultados
        jugadores = list(resultados.keys())
        puntuaciones = list(resultados.values())
        
        plt.bar(jugadores, puntuaciones, color='skyblue')
        plt.xlabel('')
        plt.ylabel('Puntaje')
        plt.title('Resultados del Trivia')
        plt.show()


# Función principal
def main():
    # Creamos una instancia de la clase Preguntas
    trivia = Preguntas()

    # Preguntamos por el número de jugadores
    num_jugadores = int(input("¿Cuántos jugadores van a participar? "))
    jugadores = []

    for i in range(num_jugadores):
        nombre = input(f"Introduce el nombre del jugador {i + 1}: ")
        jugadores.append(nombre)

    # Iniciamos el trivia y obtenemos los resultados
    resultados = trivia.hacer_preguntas(jugadores)

    # Mostramos los resultados y graficamos
    trivia.mostrar_resultados(resultados)


# Llamamos a la función principal
if __name__ == "__main__":
    main()

