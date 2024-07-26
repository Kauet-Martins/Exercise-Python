import turtle


screen = turtle.Screen() # Criando a tela 
screen.bgcolor('white') # Definindo uma cor de fundo
screen.title("spiral Turtle") # Definindo um titulo

spiral_Turtle = turtle.Turtle() # Implementando o objeto 

speed = int(input('Defina a velociade:'))

spiral_Turtle.speed(speed) # Defindo a Velocidade do ponteiro

spiral_Turtle.color('blue') # Defindo a cor do ponteiro

lenght = 10 # comprimento inicial

for i in range(50): # Criando um loop com o numero de lados da espiral

    for c in ('black', 'blue'): # loop que altera a cor do ponteiro a cada nova iniciacao 
        spiral_Turtle.color(c)
        spiral_Turtle.forward(lenght)
        spiral_Turtle.right(80)
        lenght +=5

turtle.hideturtle()
turtle.done