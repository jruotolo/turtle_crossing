from turtle import Turtle
from random import randint

STARTING_YCOR = [-230, -200, -150, -100, -50, 0, 50, 100, 150, 200, 230]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.creation_speed = 15


    def create_car(self):
        random_chance = randint(1, self.creation_speed)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.color(randint(0, 255), randint(0, 255), randint(0, 255))
            new_car.goto(350, STARTING_YCOR[randint(0, 10)])
            new_car.seth(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        if self.level % 5 == 0:
            self.creation_speed -= 1
