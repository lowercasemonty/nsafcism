import matplotlib.pyplot as plt

class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = "red"
        self.pendown = True
    
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
    
    def show(self):
        plt.show()
    
    def draw_commands(self, commands):
        pass

commands = [
("setxy", 15, 80),
("setxy", 30, 0),
("setxy", 15, -80),
("setxy", 0, 0)
]

turtle = Turtle()
turtle.draw_commands(commands)
turtle.show()