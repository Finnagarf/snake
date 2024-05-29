import pygame      #import libraies: pygame, system, & Random
import sys
import random

pygame.init()

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((width/2), (height/2))]
        self.direction = random.choice([up, down, left, right]) 
        self.color = snakeColor
        self.score = 0

    def getHeadPosition(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.getHeadPosition()
        x, y = self.direction
        new = (((current[0] + (x *gridSize)) % width), (current[1] + (y*gridSize)) % height) 
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self): #fucntion for reseting the game when you lose
        self.length = 1
        self.positions = [((width/2), (height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for pos in self.positions:
            r = pygame.Rect((pos[0], pos[1]), (gridSize,gridSize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, outlineColor, r, 1)

    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)

class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = appleColor
        self.randomizePosition()

    def randomizePosition(self):
        self.position = (random.randint(0, gridWidth - 1) * gridSize, random.randint(0, gridHeight - 1) * gridSize)
    
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridSize,gridSize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, outlineColor, r, 1)

def Grid(surface):
    for y in range(0, int(gridHeight)):
        for x in range(0, int(gridWidth)):
            if ((x + y) % 2) == 0:
                r = pygame.Rect((x * gridSize, y * gridSize), (gridSize, gridSize))
                pygame.draw.rect(surface, bgColor1, r)
            else:
                rr = pygame.Rect((x * gridSize, y * gridSize), (gridSize, gridSize))
                pygame.draw.rect(surface, bgColor2, rr)


                

#variables for game 
width = 480 
height = 480
gridSize = 20
gridWidth = width/gridSize
gridHeight = height/gridSize
bgColor1 = (31, 31, 31) # RGB values for color
bgColor2 = (15, 15, 15)
snakeColor = (222, 110, 0)
appleColor = (0, 75, 141)
outlineColor = (0, 0, 0)
fontColor = (255, 255, 255)
up = (0, -1)
down = (0, 1)
left = (-1,0)
right = (1,0)
font = pygame.font.Font('freesansbold.ttf', 20)

def main():
    pygame.init()


    clock = pygame.time.Clock() #controls game speed
    screen = pygame.display.set_mode((width, height), 0, 32)

    surface = pygame.Surface(screen.get_size()) #
    surface = surface.convert()
    Grid(surface)

    snake = Snake()
    food = Food()

    score = 0
    while True:
        clock.tick(10) #speed of snake
        snake.controls()
        Grid(surface)
        snake.move()
        if snake.getHeadPosition() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomizePosition()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = font.render("Score: {0}".format(snake.score), True, fontColor)
        screen.blit(text, (5,10))
        pygame.display.update()

main()
