from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from tkinter.messagebox import askyesno


#TODO1: Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.title("Pong Game")
screen.listen()
screen.tracer(0) # Disableing the animations


#TODO2: Create a moving paddle
r_paddle = Paddle((350, 0))
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")


#TODO3: Create another moving paddle
l_paddle = Paddle((-350, 0))
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


#TODO4: Create the ball and make it move
ball = Ball()


#TODO8: Keep scores
scoreboard = Scoreboard()


#TODO9: Reset Game
def reset_game():
    continue_game = askyesno("Game Over", "Do you want to play again?")
    if continue_game:
        scoreboard.reset_scoreboard()
        ball.reset_position()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
    else:
        game_is_on = False
        screen.bye()


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #TODO5: Detect collision with wall and bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce the ball
        ball.bounce_y()

    #TODO6: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #TODO7: Detect when paddle misses the ball
    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    #TODO10: Detect when the game is over
    if scoreboard.l_score == 2 or scoreboard.r_score == 2:
        reset_game()

screen.exitonclick()