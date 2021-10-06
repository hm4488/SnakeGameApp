# coding=utf-8
# Harsh Mathur
# Snake Game App

# Packages
import pygame
from pygame.locals import *
import time
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game App")
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + 40:
            if y2 <= y1 < y2 + 40:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        pygame.display.flip()

        # Snake eats apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # Snake dies
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Snake Dies"

    def show_game_over(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.SysFont('comic-sans', 20)
        message = font.render("To play again - press Enter", True, (255, 255, 255))
        self.surface.blit(message, (400, 300))

        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()



                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)




class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.image = pygame.image.load("images/black-check-box.png").convert()
        self.direction = 'right'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= 40
        if self.direction == 'right':
            self.x[0] += 40
        if self.direction == 'up':
            self.y[0] -= 40
        if self.direction == 'down':
            self.y[0] += 40

        self.draw()

    def draw(self):
        self.surface.fill((255, 255, 255))

        for i in range(self.length):
            self.surface.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Apple:
    def __init__(self, surface):
        self.surface = surface
        self.appleImage = pygame.image.load("images/apple.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.surface.blit(self.appleImage, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * 40
        self.y = random.randint(1, 19) * 40



if __name__ == '__main__':
    game = Game()
    game.run()
