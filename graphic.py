import turtle
turtle.setup(500, 500)
turtle.title('Hangman!')

pen = turtle.Turtle()
pen.color("orange")
pen.pensize(5)
pen.hideturtle()
        
def draw(wrongGuess):
    if (wrongGuess == 0) :
        #draw hanger
        pen.left(90)
        pen.forward(200)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
        pen.forward(20)

    if (wrongGuess == 1) :
        #draw head
        pen.right(90)
        pen.circle(10)
        pen.left(90)

    if (wrongGuess == 2) :
        #draw neck/body
        pen.penup()
        pen.forward(50)
        pen.pendown()
        pen.back(30)

    if (wrongGuess == 3) :
        #draw left arm
        pen.right(45)
        pen.forward(20)
        pen.back(20)

    if (wrongGuess == 4) :
        #draw right arm
        pen.left(90)
        pen.forward(20)
        pen.back(20)
        pen.right(45)
        pen.forward(30)

    if (wrongGuess == 5) :
        #draw left leg
        pen.right(30)
        pen.forward(15)
        pen.back(15)

    if (wrongGuess == 6) :
        #draw right leg
        pen.left(60)
        pen.forward(15)
        pen.back(15)



