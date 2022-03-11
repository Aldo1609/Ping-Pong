import turtle

#Ventana
ventana = turtle.Screen()
ventana.title("Pong by Aldo")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#Marcador
MarcadorA = 0
MarcadorB = 0

#Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_len=1, stretch_wid=5)

#Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_len=1, stretch_wid=5)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.5
pelota.dy = 0.5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A: 0		Jugador B: 0", align = "center", font=("Courier", 24, "normal"))

#Linea
division = turtle.Turtle()
division.color("white")
division.goto(0,350)
division.goto(0,-350)

#Funciones Jugador A
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

#Funciones Jugador B

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#Teclado Jugador A
ventana.listen()
ventana.onkeypress(jugadorA_up, "w")
ventana.onkeypress(jugadorA_down, "s")
#Teclado Jugador B
ventana.onkeypress(jugadorB_up, "Up")
ventana.onkeypress(jugadorB_down, "Down")


while True:
	ventana.update()

	pelota.setx(pelota.xcor() + pelota.dx)
	pelota.sety(pelota.ycor() + pelota.dy)

	#Revisa colisiones con los bordes de la ventana
	if pelota.ycor() > 290:
		pelota.dy *= -1
	if pelota.ycor() < -290:
		pelota.dy *= -1

	# Si la pelota sale por la izq o derecha, esta regresa al centro.
	if pelota.xcor() > 390:
		pelota.goto(0,0)
		pelota.dx *= -1
		MarcadorA += 1
		pen.clear()
		pen.write("Jugador A: {}		Jugador B: {}".format(MarcadorA,MarcadorB), align = "center", font=("Courier", 24, "normal"))

	if pelota.xcor() < -390:
		pelota.goto(0,0)
		pelota.dx *= -1
		MarcadorB += 1
		pen.clear()
		pen.write("Jugador A: {}		Jugador B: {}".format(MarcadorA,MarcadorB), align = "center", font=("Courier", 24, "normal"))

	if ((pelota.xcor() > 340 and pelota.xcor() < 350)
			and (pelota.ycor() < jugadorB.ycor() + 50
			and pelota.ycor() > jugadorB.ycor() - 50)):
		pelota.dx *= -1
		pelota.dy *= -1

	if ((pelota.xcor() < -340 and pelota.xcor() > -350)
			and (pelota.ycor() < jugadorA.ycor() + 50
			and pelota.ycor() > jugadorA.ycor() - 50)):
		pelota.dx *= -1
		pelota.dy *= -1