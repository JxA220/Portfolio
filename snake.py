import turtle
import random
import time

# variables

posponer = 0.1
score = 0
high_score = 0

# Creando la ventana

ventana = turtle.Screen()
ventana.title("Snake Game")
ventana.bgcolor("black")
ventana.setup(width= 600, height=600)
ventana.tracer(0)

# Cabeza de la serpiente

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Cuerpo de la serpiente

segmentos = []

# Creando la comida

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# Marcador

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0    High Score: 0", align= "center", font=("helvetica", 24 ,"normal"))

# Funciones de movimiento

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()   # ycor = cordenada y
        cabeza.sety(y + 20)  # Se actualiza el valor de la y, moviendose 20 pixeles cada vez

    elif cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)

    elif cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    elif cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

# Teclado

ventana.listen()
ventana.onkeypress(arriba,"Up")
ventana.onkeypress(izquierda,"Left")
ventana.onkeypress(derecha,"Right")
ventana.onkeypress(abajo,"Down")

# Bucle `While´ de inicio

jugar = True

while jugar == True:
    ventana.update()
    movimiento()
    time.sleep(posponer)

    # Al llegar al borde

    if cabeza.xcor() > 295 or cabeza.xcor() < -295 or cabeza.ycor() > 295 or cabeza.ycor() < -295:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        score = 0
        texto.clear()
        texto.write(f"Score: {score}    High Score: {high_score}",
                    align="center", font=("helvetica", 24, "normal"))

        # Esconder segmentos
        for segmento in segmentos:
            segmento.goto(3000,300)
        segmentos.clear()


    # Al comer la comida

    if cabeza.distance(comida) < 20:
       x = random.randint(-280,280)
       y = random.randint(-280,280)
       comida.goto(x,y)

       cuerpo = turtle.Turtle()
       cuerpo.speed(0)
       cuerpo.shape("square")
       cuerpo.color("grey")
       cuerpo.penup()
       segmentos.append(cuerpo)

       # Aumento de marcador

       score += 10

       if score > high_score:
           high_score = score

       texto.clear()
       texto.write(f"Score: {score}    High Score: {high_score}",
                   align="center", font=("helvetica", 24, "normal"))

    # Al chocar con el cuerpo

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            # Esconder segmentos

            for segmento in segmentos:
                segmento.goto(3000,3000)
            segmentos.clear()

            score = 0
            texto.clear()
            texto.write(f"Score: {score}    High Score: {high_score}",
                        align="center", font=("courier", 24, "normal"))



    # Mover el cuerpo de la serpiente

    total_seg = len(segmentos)
    for index in range(total_seg -1,0,-1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)

    if total_seg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
