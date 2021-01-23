import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)
    screen.title('Turtle Crossing')
    screen.colormode(255)

    scoreboard = Scoreboard()

    player = Player()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.move_up, 'Up')
    screen.onkey(player.move_down, 'Down')
    screen.onkey(player.move_left, 'Left')
    screen.onkey(player.move_right, 'Right')



    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()
        for car in car_manager.all_cars:
            if car.distance(player) < 25:
                game_is_on = False
                scoreboard.game_over()
                play_again = screen.textinput(title="You lost bitch", prompt='Would you like to play again?').lower()
                if play_again[0] == 'y':
                    screen.clear()
                    main()
                else:
                    screen.bye()
        if player.ycor() > 280:
            scoreboard.increase_level()
            player.player_reset()

    screen.exitonclick()

main()