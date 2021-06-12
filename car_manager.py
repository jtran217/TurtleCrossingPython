from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#This class is responsible for generating cars to travel across the screen.

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            random_y = random.randint(-240,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT









