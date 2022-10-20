from hashlib import new
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


nagini = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(nagini.move_up, "Up")
screen.onkey(nagini.move_down, "Down")
screen.onkey(nagini.move_left, "Left")
screen.onkey(nagini.move_right, "Right")

flag=True
while flag:
    screen.update()
    time.sleep(0.1)
    
    nagini.move()

    if nagini.head.distance(food) < 16:
        food.refresh()
        nagini.extend()
        score.increase_score()
        

    if nagini.head.xcor() > 280 or nagini.head.xcor() < -280 or nagini.head.ycor() > 280 or nagini.head.ycor() < -280:
        flag = False
        score.game_over()

    for segment in nagini.segments[1:]:
        if nagini.head.distance(segment) <10:
            flag = False
            score.game_over()


screen.exitonclick()



