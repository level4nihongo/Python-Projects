import pygame, random, sys, time
from pygame.math import Vector2

class SNAKE:

    def __init__(self):
        i = random.randint(5,number-5)
        j = random.randint(5,number-5)
        self.body = [Vector2(i,j), Vector2(i+1,j), Vector2(i+2,j)]
        self.direction = Vector2(0,1)
        self.newblock = False

    def drawsnake(self):
        for e in self.body:
            part = pygame.Rect(e.x * size, e.y * size, size, size)
            pygame.draw.rect(scr, snake_color, part)

    def move(self):
        if self.newblock:
            bodycopy = self.body
            bodycopy.insert(0, bodycopy[0]+ self.direction)
            self.body = bodycopy
            self.newblock = False

        else:
            bodycopy = self.body[:-1]
            bodycopy.insert(0, bodycopy[0]+ self.direction)
            self.body = bodycopy

    def makebigger(self):
        self.newblock = True

class FOOD:
    def __init__(self):
        self.newposition()

    def drawfood(self):
        fruit = pygame.Rect(self.pos.x * size, self.pos.y * size, size, size)
        scr.blit(appple, fruit)
        #pygame.draw.rect(scr, food_color, fruit)

    def newposition(self):
        self.x = random.randint(1,number-1)
        self.y = random.randint(1,number-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:

    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        if moving == True:
            self.snake.move()
            self.checkcollision()
            self.check_fail()

    def drawelements(self):
        self.food.drawfood()
        self.snake.drawsnake()

    def checkcollision(self):
        if self.food.pos == self.snake.body[0]:
            print("eated the food")
            self.food.newposition()
            self.snake.makebigger()

    def check_fail(self):

        if not 0 <= self.snake.body[0].x <= number:
            self.gameover()

        if not 0 <= self.snake.body[0].y <= number:
            self.gameover()

        for e in self.snake.body[1:]:
            if self.snake.body[0] == e:
                self.gameover()

    def gameover(self):
        #time.sleep()
        pygame.quit()
        sys.exit()

#start pygame
pygame.init()
size = 20
number = 30
scr = pygame.display.set_mode((size*number,size*number))
clock = pygame.time.Clock()
apple = pygame.image.load('apple.png').convert_alpha()

snake_color = (255,255,220)
food_color = (200, 40, 100)

main = MAIN()

screenupdate = pygame.USEREVENT
pygame.time.set_timer(screenupdate, 120)
moving = True
while True:
    #draw everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenupdate:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction != Vector2(0, 1):
                    main.snake.direction = Vector2(0, -1)
                    moving = True
            if event.key == pygame.K_DOWN:
                if main.snake.direction != Vector2(0, -1):
                    main.snake.direction = Vector2(0, 1)
                    moving = True
            if event.key == pygame.K_RIGHT:
                if main.snake.direction != Vector2(-1, 0):
                    main.snake.direction = Vector2(1, 0)
                    moving = True
            if event.key == pygame.K_LEFT:
                if main.snake.direction != Vector2(1, 0):
                    main.snake.direction = Vector2(-1, 0)
                    moving = True
            if event.key == pygame.K_SPACE:
                main.snake.direction = Vector2(0, 0)
                moving = False
    scr.fill(pygame.Color('pink'))
    main.snake.drawsnake()
    main.food.drawfood()
    pygame.display.update()
    clock.tick(120)
