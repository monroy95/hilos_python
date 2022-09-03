import random
import threading
import turtle
import time


def createTurtlePlayer(color, startx, starty):
    """funcion para crear un objeto grafico con turtle

    Args:
        color (str): color para el objeto
        startx (int): posicion inicial para x
        starty (int): posicion inicial para y

    Returns:
        object: objeto turtle
    """
    player = turtle.Turtle()
    player.color(color)
    player.shape("square")  # definicion de figura
    player.penup()  # Se levanta el pen para dibujar
    player.goto(startx, starty)  # Se posiciona sobre la posicion
    player.pendown()  # baja el pen para dibujar
    return player  # turtle carrito object.


def car_one(p1, finishLineX):
    """metodo para el carrito 1, se usa para moverlo de posicion

    Args:
        p1 (object): objeto turtle (carrito)
        finishLineX (int): limite de pista
    """
    while True:
        time.sleep(0.2)
        p1.forward(random.randint(5, 10))
        if p1.pos()[0] >= finishLineX:
            p1.write('    Llego carrito #1!', font=('consolas', 12))
            break


def car_two(p2, finishLineX):
    """metodo para el carrito 2, se usa para moverlo de posicion

    Args:
        p2 (object): objeto turtle (carrito)
        finishLineX (int): limite de pista
    """
    while True:
        time.sleep(0.2)
        p2.forward(random.randint(5, 10))
        if p2.pos()[0] >= finishLineX:
            p2.write('    Llego carrito #2!', font=('consolas', 12))
            break


def car_three(p3, finishLineX):
    """metodo para el carrito 3, se usa para moverlo de posicion

    Args:
        p3 (object): objeto turtle (carrito)
        finishLineX (int): limite de pista
    """
    while True:
        time.sleep(0.2)
        p3.forward(random.randint(5, 10))
        if p3.pos()[0] >= finishLineX:
            p3.write('    Llego carrito #3!', font=('consolas', 12))
            break


def car_four(p4, finishLineX):
    """metodo para el carrito 4, se usa para moverlo de posicion

    Args:
        p4 (object): objeto turtle (carrito)
        finishLineX (int): limite de pista
    """
    while True:
        time.sleep(0.2)
        p4.forward(random.randint(5, 10))
        if p4.pos()[0] >= finishLineX:
            p4.write('    Llego carrito #4!', font=('consolas', 12))
            break


def carreritas():
    """menu principal para carrera
    """
    myscreen = turtle.Screen()

    myscreen.bgcolor('#21252b')
    myscreen.setup(0.5, 0.5)  # posicion inicial de ventana
    myscreen.title('Carreritas')

    pen = turtle.Turtle()

    pen.speed(0)  # velocidad inicial
    pen.penup()
    pen.goto(-200, 200)  # posicion dentro de la ventana
    pen.pendown()

    for i in range(1, 11):  # dibuja las lineas de 1 al 10
        pen.write(i, font=('Arial', 10))  # dibuja los numero de 1 al 10
        pen.color('white')
        pen.setheading(-90)  # para dibujar verticalmente
        pen.forward(250)  # dibujar linea de 250px
        if i == 10:
            pen.write(" META", font=('Arial', 14))
        pen.back(250)
        pen.penup()
        pen.setheading(0)
        pen.forward(50)  # espacio de 50 píxeles entre cada línea
        pen.down()

    pen.pendown()
    pen.penup()
    pen.goto(0, 260)
    pen.write("EQUIPO #3", move=True, align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -80)
    pen.write("Mario Joel Monroy Canizales 0900-16-3378", move=True, align="center", font=("Courier", 12, "normal"))
    pen.goto(0, -100)
    pen.write("Eduvijes de Jesus Lazaro Orellana 0900-18-1755", move=True, align="center", font=("Courier", 12, "normal"))
    pen.goto(0, -120)
    pen.write("Milton Javier Navarro Fuentes 0900-21-11576", move=True, align="center", font=("Courier", 12, "normal"))
    pen.goto(0, -140)
    pen.write("Andrés Eduardo León Sosa 0900-20-2395", move=True, align="center", font=("Courier", 12, "normal"))
    pen.goto(0, -160)
    pen.write("Karen Sofia Baltazar Mejia 0900-19-17152", move=True, align="center", font=("Courier", 12, "normal"))

    pen.goto(0, -190)
    pen.write("NOTA: DEBE ESPERAR QUE TERMINE LA CARRERA PARA CERRAR EL PROGRAMA, DE LO CONTRARIO SE ENCICLARA EL PROCESO",
              move=True, align="center", font=("Courier", 14, "normal"))

    finishLineX = 250

    p1 = createTurtlePlayer('red', -250, 150)  # objeto de color rojo en la posición x antes de la primera línea y en la posición y 150
    p2 = createTurtlePlayer('blue', -250, 100)  # objeto de color azul en la posición x antes de la primera línea y en la posición y 100
    p3 = createTurtlePlayer('orange', -250, 50)  # objeto de color anaranjado en la posición x antes de la primera línea y en la posición y 50
    p4 = createTurtlePlayer('green', -250, 0)  # objeto de color verde en la posición x antes de la primera línea y en la posición y 0

    try:
        # Definicion de los hilos
        car1 = threading.Thread(name='Carrito_1', target=car_one, args=(p1, finishLineX,))
        car2 = threading.Thread(name='Carrito_2', target=car_two, args=(p2, finishLineX,))
        car3 = threading.Thread(name='Carrito_3', target=car_three, args=(p3, finishLineX,))
        car4 = threading.Thread(name='Carrito_4', target=car_four, args=(p4, finishLineX,))

        # arranque ejecucion de hilos
        car1.start()
        car2.start()
        car3.start()
        car4.start()

        # car1.join()
        # car2.join()
        # car3.join()
        # car4.join()

        turtle.done()
        print('TERMINO LA CARRERA!')

    except Exception as e:
        print(f"Error, mas detalles en {e}")


if __name__ == '__main__':
    carreritas()
